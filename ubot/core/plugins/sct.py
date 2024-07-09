from gc import get_objects

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultArticle, InputTextMessageContent)

from ubot import *


async def msg_cmd(client, message):
    if not message.reply_to_message:
        return await message.reply(
            f"<code>{message.text}</code> [balas pesan pengguna - text]"
        )
    text = f"secret {id(message)}"
    await message.delete()
    x = await client.get_inline_bot_results(bot.me.username, text)
    await message.reply_to_message.reply_inline_bot_result(x.query_id, x.results[0].id)


async def secret_inline(client, q):
    m = [obj for obj in get_objects() if id(obj) == int(q.query.split()[1])][0]
    await client.answer_inline_query(
        q.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="pesan rahasia!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Private Message",
                                    url=f"https://t.me/{bot.me.username}?start=secretMsg_{int(q.query.split(None, 1)[1])}",
                                )
                            ],
                        ]
                    ),
                    input_message_content=InputTextMessageContent(
                        f"<b>Pesan Untuk Anda :</b> <a href=tg://user?id={m.reply_to_message.from_user.id}>{m.reply_to_message.from_user.first_name} {m.reply_to_message.from_user.last_name or ''}</a>"
                    ),
                )
            )
        ],
    )
