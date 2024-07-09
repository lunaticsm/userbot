import asyncio
import importlib
from datetime import datetime

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *

from ubot import *


async def need_api(client, callback_query):
    user_id = callback_query.from_user.id
    if len(ubot._ubot) > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("Tutup", callback_data="0_cls")],
        ]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            f"""
<b>❌ Tidak Membuat Userbot !</b>

<b>📚 Karena Telah Mencapai Yang Telah Di Tentukan : {len(ubot._ubot)}</b>

<b>👮‍♂ Silakan Hubungi Admin . </b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if user_id not in await get_prem():
        buttons = [
            [InlineKeyboardButton("➡️ Lanjutkan", callback_data="bayar_dulu")],
            [InlineKeyboardButton("❌ Batalkan", callback_data=f"home {user_id}")],
        ]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            MSG.POLICY(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        await bikin_ubot(client, callback_query)


async def payment_userbot(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = Button.plus_minus(1, user_id)
    await callback_query.message.delete()
    return await bot.send_message(
        user_id,
        MSG.TEXT_PAYMENT(30, 30, 1),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


async def bikin_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    await callback_query.message.delete()
    try:
        phone = await bot.ask(
            user_id,
            (
                "<b>Silahkan masukkan Nomor Telegram anda.</b>\n"
                "\n<b>Gunakan /cancel untuk Membatalkan Proses Membuat Userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "Pembatalan Otomatis")
    if await is_cancel(callback_query, phone.text):
        return
    phone_number = phone.text
    new_client = Ubot(
        name=str(callback_query.id),
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=False,
    )
    get_otp = await bot.send_message(user_id, "<b>Mengirim Kode Otp...</b>")
    await new_client.connect()
    try:
        code = await new_client.send_code(phone_number.strip())
    except ApiIdInvalid as AID:
        await get_otp.delete()
        return await bot.send_message(user_id, AID)
    except PhoneNumberInvalid as PNI:
        await get_otp.delete()
        return await bot.send_message(user_id, PNI)
    except PhoneNumberFlood as PNF:
        await get_otp.delete()
        return await bot.send_message(user_id, PNF)
    except PhoneNumberBanned as PNB:
        await get_otp.delete()
        return await bot.send_message(user_id, PNB)
    except PhoneNumberUnoccupied as PNU:
        await get_otp.delete()
        return await bot.send_message(user_id, PNU)
    except Exception as error:
        await get_otp.delete()
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    try:
        sent_code = {
            SentCodeType.APP: "<a href=tg://openmessage?user_id=777000>Akun Telegram</a> ʀᴇsᴍɪ",
            SentCodeType.SMS: "Sms Anda",
            SentCodeType.CALL: "Panggilan Telepon",
            SentCodeType.FLASH_CALL: "Panggilan Kilat Telepon",
            SentCodeType.FRAGMENT_SMS: "Fragment Sms",
            SentCodeType.EMAIL_CODE: "Email Sms",
        }
        await get_otp.delete()
        otp = await bot.ask(
            user_id,
            (
                "<b>Silakan Periksa Kode OTP dari <a href=tg://openmessage?user_id=777000>Akun Telegram</a> Resmi. Kirim Kode OTP ke sini setelah membaca Format di bawah ini.</b>\n"
                "\nJika Kode OTP adalah <code>12345</code> Tolong <b>[ TAMBAHKAN SPASI ]</b> kirimkan Seperti ini <code>1 2 3 4 5</code>\n"
                "\n<b>Gunakan /cancel untuk Membatalkan Proses Membuat Userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "Waktu Telah Habis")
    if await is_cancel(callback_query, otp.text):
        return
    otp_code = otp.text
    try:
        await new_client.sign_in(
            phone_number.strip(),
            code.phone_code_hash,
            phone_code=" ".join(str(otp_code)),
        )
    except PhoneCodeInvalid as PCI:
        return await bot.send_message(user_id, PCI)
    except PhoneCodeExpired as PCE:
        return await bot.send_message(user_id, PCE)
    except BadRequest as error:
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    except SessionPasswordNeeded:
        try:
            two_step_code = await bot.ask(
                user_id,
                "<b>Akun anda Telah mengaktifkan Verifikasi Dua Langkah. Silahkan Kirimkan Passwordnya.\n\nGunakan /cancel untuk Membatalkan Proses Membuat Userbot</b>",
                timeout=300,
            )
        except asyncio.TimeoutError:
            return await bot.send_message(user_id, "ᴘᴇᴍʙᴀᴛᴀʟᴀɴ ᴏᴛᴏᴍᴀᴛɪs")
        if await is_cancel(callback_query, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await new_client.check_password(new_code)
            await set_two_factor(user_id, new_code)
        except Exception as error:
            return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    session_string = await new_client.export_session_string()
    await new_client.disconnect()
    new_client.storage.session_string = session_string
    new_client.in_memory = False
    bot_msg = await bot.send_message(
        user_id,
        "Tunggu proses selama 1-5 menit..",
        disable_web_page_preview=True,
    )
    await new_client.start()
    await add_ubot(
        user_id=int(new_client.me.id),
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session_string,
    )
    #await set_uptime(new_client.me.id, time())
    if callback_query.from_user.id not in await get_seles():
        await remove_prem(callback_query.from_user.id)
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"ubot.modules.{mod}"))
    text_done = f"<b>🔥 {bot.me.mention} Berhasil Di Aktifkan Di Akun :\n<a href=tg://openmessage?user_id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> > <code>{new_client.me.id}</code></b> "
    await bot_msg.edit(text_done)
    try:
        await new_client.join_chat("alterbase2")
        await new_client.join_chat("sexualredroom")
    except UserAlreadyParticipant:
        pass
    return await bot.send_message(
        LOG_UBOT,
        f"""
<b>❏ Userbot Diaktifkan</b>
<b> ├ Akun :</b> <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> 
<b> ╰ ID :</b> <code>{new_client.me.id}</code>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Cek Kadaluarsa",
                        callback_data=f"cek_masa_aktif {new_client.me.id}",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
    

async def next_prev_ubot(client, callback_query):
    query = callback_query.data.split()
    count = int(query[1])
    if query[0] == "next_ub":
        if count == len(ubot._ubot) - 1:
            count = 0
        else:
            count += 1
    elif query[0] == "prev_ub":
        if count == 0:
            count = len(ubot._ubot) - 1
        else:
            count -= 1
    await callback_query.edit_message_text(
        await MSG.USERBOT(count),
        reply_markup=InlineKeyboardMarkup(
            Button.userbot(ubot._ubot[count].me.id, count)
        ),
    )

async def tools_userbot(client, callback_query):
    user_id = callback_query.from_user.id
    query = callback_query.data.split()
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ Gausa di klik bang {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    X = ubot._ubot[int(query[1])]
    if query[0] == "get_otp":
        async for otp in X.search_messages(777000, limit=1):
            try:
                if not otp.text:
                    await callback_query.answer("❌ Kode tidak ditemukan", True)
                else:
                    await callback_query.edit_message_text(
                        otp.text,
                        reply_markup=InlineKeyboardMarkup(
                            Button.userbot(X.me.id, int(query[1]))
                        ),
                    )
                    await X.delete_messages(X.me.id, otp.id)
            except Exception as error:
                return await callback_query.answer(error, True)
    elif query[0] == "get_phone":
        try:
            return await callback_query.edit_message_text(
                f"<b>📲 Nomer telepon <code>{X.me.id}</code> adalah <code>{X.me.phone_number}</code></b>",
                reply_markup=InlineKeyboardMarkup(
                    Button.userbot(X.me.id, int(query[1]))
                ),
            )
        except Exception as error:
            return await callback_query.answer(error, True)
    elif query[0] == "get_faktor":
        code = await get_two_factor(X.me.id)
        if code == None:
            return await callback_query.answer(
                "🔐 Kode verifikasi 2 langkah tidak ditemukan", True
            )
        else:
            return await callback_query.edit_message_text(
                f"<b>🔐 Kode verifikasi 2 langkah pengguna <code>{X.me.id}</code> adalah : <code>{code}</code></b>",
                reply_markup=InlineKeyboardMarkup(
                    Button.userbot(X.me.id, int(query[1]))
                ),
            )
    

async def cek_ubot(client, callback_query):
    await bot.send_message(
        callback_query.from_user.id,
        await MSG.USERBOT(0),
        reply_markup=InlineKeyboardMarkup(Button.userbot(ubot._ubot[0].me.id, 0)),
    )


async def cek_userbot_expired(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    expired = await get_expired_date(user_id)
    try:
        xxxx = (expired - datetime.now()).days
        return await callback_query.answer(f"⏳ Tinggal {xxxx} hari lagi", True)
    except:
        return await callback_query.answer("✅ Sudah tidak aktif", True)

async def hapus_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ ꜱᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪꜰᴊᴀɴɢᴀɴ ᴅɪᴋʟɪᴋ ʙᴏꜱꜱ {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    try:
        show = await bot.get_users(callback_query.data.split()[1])
        get_id = show.id
        get_mention = f"<a href=tg://user?id={get_id}>{show.first_name} {show.last_name or ''}</a>"
    except Exception:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"<a href=tg://user?id={get_id}>Userbot</a>"
    for X in ubot._ubot:
        if get_id == X.me.id:
            await X.unblock_user(bot.me.username)
            for chat in await get_chat(X.me.id):
                await remove_chat(X.me.id, chat)
            await rm_all(X.me.id)
            await remove_ubot(X.me.id)
            await rem_expired_date(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            await bot.send_message(
                OWNER_ID, f"<b> ✅ {get_mention} Berhasil Di Hapus Dari Database</b>"
            )
            return await bot.send_message(
                X.me.id, "<b>💬 Masa Aktif Anda Telah Habis"
            )


async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(
            callback_query.from_user.id, "<b>Proses Di Batalkan !</b>"
        )
        return True
    return False
