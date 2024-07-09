from gc import get_objects
from io import BytesIO

from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

from ubot import *


async def addnote_cmd(client, message):
    note_name = get_arg(message)
    reply = message.reply_to_message
    if not reply:
        return await message.reply(
            "<b>Gunakan format :</b> <code>addnote</code> [nama catatan] [balas ke pesan].",
        )
    if await get_note(client.me.id, note_name):
        return await message.reply(f"<b>Catatan <code>{note_name}</code> sudah ada.</b>")
    copy = await client.copy_message(client.me.id, message.chat.id, reply.id)
    await save_note(client.me.id, note_name, copy.id)
    await message.reply(f"<b>Catatan <code>{note_name}</code> berhasil disimpan.</b>")


async def get_cmd(client, message):
    note_name = get_arg(message)
    if not note_name:
        return await message.reply("Cantumkan nama catatan")
    note = await get_note(client.me.id, note_name)
    if not note:
        return await message.reply(f"Catatan dengan nama {note_name} tidak ada.")
    note_id = await client.get_messages(client.me.id, note)
    if note_id.text:
        if "~" in note_id.text:
            try:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"get_notes {id(message)}"
                )
                msg = message.reply_to_message or message
                await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=msg.id,
                )
            except Exception as error:
                return await message.reply(error)
        else:
            msg = message.reply_to_message or message
            await client.copy_message(
                message.chat.id,
                client.me.id,
                note,
                reply_to_message_id=msg.id,
            )
    else:
        msg = message.reply_to_message or message
        await client.copy_message(
            message.chat.id,
            client.me.id,
            note,
            reply_to_message_id=msg.id,
        )


async def get_notes_button(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = [obj for obj in get_objects() if id(obj) == _id][0]
    get_note_id = await get_note(m._client.me.id, m.text.split()[1])
    note_id = await m._client.get_messages(m._client.me.id, get_note_id)
    buttons, text_button = await notes_create_button(note_id.text)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get notes!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(text_button),
                )
            )
        ],
    )


async def delnote_cmd(client, message):
    note_name = get_arg(message)
    if not note_name:
        return await message.reply(
            "<b>Gunakan format :</b> <code>delnote</code> [nama catatan]",
        )
    note = await get_note(client.me.id, note_name)
    if not note:
        return await message.reply(
            f"<b>Catatan dengan nama <code>{note_name}</code> tidak ditemukan.</b>",
        )
    await rm_note(client.me.id, note_name)
    await message.reply(f"<b>Catatan <code>{note_name}</code> berhasil dihapus.</b>")

    await client.delete_messages(client.me.id, [int(note), int(note) + 1])



async def notes_cmd(client, message):
    msg = f"<b>๏ Daftar Catatan :</b>\n\n"
    semua = await all_notes(client.me.id)
    if not semua:
        return await message.reply("Tidak ada catatan tersimpan .")
    else:
        for notes in semua:
            msg += f"• <code>{notes}</code>\n"
    if int(len(str(msg))) > 4096:
        with BytesIO(str.encode(str(msg))) as out_file:
            out_file.name = "notes.txt"
            await message.reply_document(
                document=out_file,
            )
    await message.reply(msg)
