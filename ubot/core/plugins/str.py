import asyncio
from datetime import datetime
from gc import get_objects
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ubot import *


async def send_msg_to_owner(client, message):
    if message.from_user.id == OWNER_ID:
        return
    else:
        buttons = [
            [
                InlineKeyboardButton(
                    "👤 ᴘʀᴏꜰɪʟ", callback_data=f"profil {message.from_user.id}"
                ),
                InlineKeyboardButton(
                    "ᴊᴀᴡᴀʙ 💬", callback_data=f"jawab_pesan {message.from_user.id}"
                ),
            ],
        ]
        await client.send_message(
            OWNER_ID,
            f"<a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>\n\n<code>{message.text}</code>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )

async def absen(client, message):
    await message.reply("<b>Kyaaaaa>,<</b>")


async def sayang(client, message):
    await message.reply("<b>Iyaaa sayanggg kenapaa?🥰</b>")


async def akugtgkn(client, message):
    await message.reply("<b>Iyaaa uputtt gantengg bangettt😘😍🥰</b>")


async def anara(client, message):
    await message.reply("<b>Punyaa Uputtt😘</b>")

async def reak(client, message):
    await client.send_reaction(message.chat.id, message.id, "🦄")


async def ping_cmd(client, message):
    uptime = await get_time((time() - start_time))
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    _ping = f"""
<b><emoji id=6339136407637855286>😎</emoji> Pong !!
</b> {str(delta_ping).replace('.', ',')} ms
"""
    await message.reply(_ping)


async def start_cmd(client, message):
    await add_served_user(message.from_user.id)
    await send_msg_to_owner(client, message)
    if len(message.command) < 2:
        buttons = Button.start(message)
        msg = MSG.START(message)
        await message.reply(msg, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        txt = message.text.split(None, 1)[1]
        msg_id = txt.split("_", 1)[1]
        send = await message.reply("<b>Tunggu Sebentar...</b>")
        if "secretMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ ᴇʀʀᴏʀ:</b> <code>{error}</code>")
            user_or_me = [m.reply_to_message.from_user.id, m.from_user.id]
            if message.from_user.id not in user_or_me:
                return await send.edit(
                    f"<b>❌ Jangan di Klik ngentod, anjeng lu emang🖕 <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
                )
            else:
                text = await client.send_message(
                    message.chat.id,
                    m.text.split(None, 1)[1],
                    protect_content=True,
                    reply_to_message_id=message.id,
                )
                await send.delete()
                await asyncio.sleep(120)
                await message.delete()
                await text.delete()
        elif "copyMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ ᴇʀʀᴏʀ:</b> <code>{error}</code>")
            id_copy = int(m.text.split()[1].split("/")[-1])
            if "t.me/c/" in m.text.split()[1]:
                chat = int("-100" + str(m.text.split()[1].split("/")[-2]))
            else:
                chat = str(m.text.split()[1].split("/")[-2])
            try:
                get = await client.get_messages(chat, id_copy)
                await get.copy(message.chat.id, reply_to_message_id=message.id)
                await send.delete()
            except Exception as error:
                await send.edit(error)
