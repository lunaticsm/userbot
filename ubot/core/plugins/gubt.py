import random
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,
                            InputTextMessageContent)

from ubot import *


async def getubot_cmd(client, message):
    msg = await message.reply("<b>Tunggu Sebentar...</b>", quote=True)
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"ambil_ubot"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
        await msg.delete()
    except Exception as error:
        await msg.edit(error)


async def getubot_query(client, inline_query):
    msg = await MSG.USERBOT(0)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="💬",
                    reply_markup=InlineKeyboardMarkup(Button.ambil_akun(ubot._ubot[0].me.id, 0)),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )

async def close_usernya(client, callback_query):
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for x in ubot._ubot:
        if callback_query.from_user.id == int(x.me.id):
            await x.delete_messages(
                unPacked.chat_id, unPacked.message_id
            )
