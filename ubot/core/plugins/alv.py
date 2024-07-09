import random
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,
                            InputTextMessageContent)

from ubot import *


async def alive_cmd(client, message):
    msg = await message.reply("<b>Tunggu Sebentar...</b>", quote=True)
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"alive {message.id} {client.me.id}"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
        await msg.delete()
    except Exception as error:
        await msg.edit(error)


async def alive_query(client, inline_query):
    get_id = inline_query.query.split()
    for my in ubot._ubot:
        if int(get_id[2]) == my.me.id:
            try:
                peer = my._get_my_peer[my.me.id]
                users = len(peer["pm"])
                group = len(peer["gc"])
            except Exception:
                users = random.randrange(await my.get_dialogs_count())
                group = random.randrange(await my.get_dialogs_count())
            get_exp = await get_expired_date(my.me.id)
            exp = get_exp.strftime("%d-%m-%Y")
            if my.me.id in DEVS:
                status = "<b>Premium</b> <code>[Hokage]</code>"
            elif my.me.id in await get_seles():
                status = "<b>Premium</b> <code>[Anbu]</code>"
            else:
                status = "<b>Premium</b> <code>[Genin]</code>"
            button = Button.alive(get_id)
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            uptime = await get_time((time() - start_time))
            msg = f"""
<b>Xuta-Userbot</b>
    <b>status:</b> {status} 
      <b>dc_id:</b> <code>{my.me.dc_id}</code>
      <b>ping_dc:</b> <code>{str(ping).replace('.', ',')} ms</code>
      <b>peer_users:</b> <code>{users} users</code>
      <b>peer_group:</b> <code>{group} group</code>
      <b>ubot_uptime:</b> <code>{uptime}</code>
      <b>expires_on:</b> <code>{exp}</code>
"""
            await client.answer_inline_query(
                inline_query.id,
                cache_time=0,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="💬",
                            reply_markup=InlineKeyboardMarkup(button),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )


async def alive_close(client, callback_query):
    get_id = callback_query.data.split()
    if not callback_query.from_user.id == int(get_id[2]):
        return await callback_query.answer(
            f"❌ Mau ngapain bang {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for my in ubot._ubot:
        if callback_query.from_user.id == int(my.me.id):
            await my.delete_messages(
                unPacked.chat_id, [int(get_id[1]), unPacked.message_id]
            )
