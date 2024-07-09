import re

from pyrogram.types import *

from ubot import *


async def help_cmd(client, message):
    if not get_arg(message):
        try:
            x = await client.get_inline_bot_results(bot.me.username, "help")
            await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            await message.reply(error)
    else:
        nama = get_arg(message)
        if get_arg(message) in HELP_COMMANDS:
            prefix = await get_prefix(client.me.id)
            await message.reply(
                HELP_COMMANDS[get_arg(message)].__HELP__.format(
                    next((p) for p in prefix)
                )
                + "\n<b> ® ? </b>",
                quote=True,
            )
        else:
            await message.reply(
                f"<b>❌ Tidak ada modul bernama <code>{nama}</code></b>"
            )



async def menu_inline(client, inline_query):
    user_id = inline_query.from_user.id
    emut = await get_pref(user_id)
    if emut is not None:
        msg = "<b>Help Modules\n     Prefixes: <code>{}</code>\n     Commands: <code>{}</code></b>".format(emut[0], len(HELP_COMMANDS))
    elif emut == [""]:
        msg = "<b>Help Modules\n     Prefixes: `None`\n     Commands: <code>{}</code></b>".format(len(HELP_COMMANDS))
    else:
        msg = "<b>Help Modules\n     Prefixes: `None`\n     Commands: <code>{}</code></b>".format(len(HELP_COMMANDS))
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Menu!",
                    reply_markup=InlineKeyboardMarkup(
                        paginate_modules(0, HELP_COMMANDS, "help")
                    ),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )



async def menu_callback(client, callback_query):
    mod_match = re.match(r"help_module\((.+?)\)", callback_query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", callback_query.data)
    next_match = re.match(r"help_next\((.+?)\)", callback_query.data)
    back_match = re.match(r"help_back", callback_query.data)
    user_id = callback_query.from_user.id
    prefix = await get_prefix(user_id)
    emut = await get_pref(user_id)
    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = f"<b>{HELP_COMMANDS[module].__HELP__}</b>\n".format(next((p) for p in prefix))
        #text = HELP_COMMANDS[module].__HELP__
        button = [[InlineKeyboardButton("Kembali", callback_data="help_back")]]
        await callback_query.edit_message_text(
            text=text + "\n<b> ® ? </b>",
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    if emut is not None:
        top_text = "<b>Help Modules\n     Prefixes: <code>{}</code>\n     Commands: <code>{}</code></b>".format(emut[0], len(HELP_COMMANDS))

    elif emut == [""]:
        top_text = "<b>Help Modules\n     Prefixes: `None`\n     Commands: <code>{}</code></b>".format(len(HELP_COMMANDS))
    else:
        top_text = "<b>Help Modules\n     Prefixes: `None`\n     Commands: <code>{}</code></b>".format(len(HELP_COMMANDS))
    
    if prev_match:
        curr_page = int(prev_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
    if next_match:
        next_page = int(next_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
    if back_match:
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
