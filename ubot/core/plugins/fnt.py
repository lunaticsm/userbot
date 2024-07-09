from gc import get_objects

from pykeyboard import InlineKeyboard
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from ubot import *


async def font_message(client, message):
    if message.reply_to_message:
        if message.reply_to_message.text:
            query = id(message)
        else:
            return await message.reply("Harap reply ke teks")
    else:
        if len(message.command) < 2:
            return await message.reply(f"{message.text} [reply/teks]")
        else:
            query = id(message)
    try:
        x = await client.get_inline_bot_results(bot.me.username, f"get_font {query}")
        return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        return await message.reply(str(error))


async def font_inline(client, inline_query):
    get_id = int(inline_query.query.split(None, 1)[1])
    buttons = InlineKeyboard(row_width=3)
    keyboard = []
    for X in query_fonts[0]:
        keyboard.append(
            InlineKeyboardButton(X, callback_data=f"get {get_id} {query_fonts[0][X]}")
        )
    buttons.add(*keyboard)
    buttons.row(InlineKeyboardButton("➡️", callback_data=f"next {get_id}"))
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get font!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(
                        "<b>👇 Silahkan pilih salah satu font di bawah</b>"
                    ),
                )
            )
        ],
    )


async def font_next(client, callback_query):
    try:
        get_id = int(callback_query.data.split()[1])
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in query_fonts[1]:
            keyboard.append(
                InlineKeyboardButton(
                    X, callback_data=f"get {get_id} {query_fonts[1][X]}"
                )
            )
        buttons.add(*keyboard)
        buttons.row(InlineKeyboardButton("⬅️", callback_data=f"prev {get_id}"))
        return await callback_query.edit_message_reply_markup(reply_markup=buttons)
    except Exception as error:
        return await callback_query.answer(f"❌ Error: {error}", True)


async def font_prev(client, callback_query):
    try:
        get_id = int(callback_query.data.split()[1])
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in query_fonts[0]:
            keyboard.append(
                InlineKeyboardButton(
                    X, callback_data=f"get {get_id} {query_fonts[0][X]}"
                )
            )
        buttons.add(*keyboard)
        buttons.row(InlineKeyboardButton("➡️", callback_data=f"next {get_id}"))
        return await callback_query.edit_message_reply_markup(reply_markup=buttons)
    except Exception as error:
        return await callback_query.answer(f"❌ Error: {error}", True)


async def font_callback(client, callback_query):
    try:
        q = int(callback_query.data.split()[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        new = str(callback_query.data.split()[2])
        if m.reply_to_message:
            text = m.reply_to_message.text
        else:
            text = m.text.split(None, 1)[1]
        get_new_font = gens_font(new, text)
        return await callback_query.edit_message_text(get_new_font)
    except Exception as error:
        return await callback_query.answer(f"❌ Error: {error}", True)
