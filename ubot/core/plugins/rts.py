import importlib
import random
from datetime import datetime, timedelta

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from ubot import *


async def login_cmd(client, message):
    info = await message.reply("<b>Tunggu Sebentar...</b>", quote=True)
    if len(message.command) < 3:
        return await info.edit(
            f"<code>{message.text}</code> <b>ʜᴀʀɪ - sᴛʀɪɴɢ ᴘʏʀᴏɢʀᴀᴍ</b>"
        )
    try:
        ub = Ubot(
            name=f"ubot_{random.randrange(999999)}",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[2],
        )
        await ub.start()
        for mod in loadModule():
            importlib.reload(importlib.import_module(f"ubot.modules.{mod}"))
        now = datetime.now(timezone("Asia/Jakarta"))
        expire_date = now + timedelta(days=int(message.command[1]))
        await set_expired_date(ub.me.id, expire_date)
        await add_ubot(
            user_id=int(ub.me.id),
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[1],
        )
        buttons = [
            [
                InlineKeyboardButton(
                    "Cek Kadaluarsa",
                    callback_data=f"cek_masa_aktif {ub.me.id}",
                )
            ],
        ]
        await bot.send_message(
            LOG_UBOT,
            f"""
<b>❏ Userbot Diaktifkan</b>
<b> ├ Akun:</b> <a href=tg://user?id={ub.me.id}>{ub.me.first_name} {ub.me.last_name or ''}</a> 
<b> ╰ ID:</b> <code>{ub.me.id}</code>
""",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
        )
        return await info.edit(
            f"<b>✅ Berhasil Login Di Akun: <a href='tg://user?id={ub.me.id}'>{ub.me.first_name} {ub.me.last_name or ''}</a></b>"
        )
    except Exception as error:
        return await info.edit(f"<code>{error}</code>")


async def restart_cmd(client, message):
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
    msg = await message.reply("<b>Tunggu Sebentar...</b>", quote=True)
    if message.from_user.id not in ubot._get_my_id:
        return await msg.edit(
            f"<b>Anda bukan pengguna @{bot.me.username}</b>"
        )
    for x in ubot._ubot:
        if message.from_user.id == x.me.id:
            try:
                if ubot_.is_connected:
                    await ubot_.disconnect()
                else:
                    ubot_.in_memory = False
                    await ubot_.start()
                    for mod in loadModule():
                        importlib.reload(importlib.import_module(f"ubot.modules.{mod}"))
                    return await msg.edit(f"<b>✅ Berhasil Di Restart</b>")
            except Exception as e:
                return await msg.edit(f"**Error : `{e}`**")




async def restart_cmd2(client, message):
    msg = await message.reply("<b>Processing...</b>", quote=True)
    if message.from_user.id not in ubot._get_my_id:
        return await msg.edit(
            f"<b>Anda bukan pengguna @{bot.me.username}!!</b>"
        )
    for X in ubot._ubot:
        if message.from_user.id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"ubot.modules.{mod}")
                            )
                        return await msg.edit(
                            f"<b>✅ Berhasil Di Restart {UB.me.first_name} {UB.me.last_name or ''} | {UB.me.id}.</b>"
                        )
                    except Exception as error:
                        return await msg.edit(f"<b>{error}</b>")