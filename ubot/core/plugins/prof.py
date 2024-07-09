import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from ubot import *



async def unblock_user_func(client, message):
    user_id = await extract_user(message)
    tex = await message.reply("Processing...")
    if not user_id:
        return await tex.edit("Provide a username or reply to a message to unblock.")
    if user_id == client.me.id:
        return await tex.edit("Ok done.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<b>Berhasil membuka blokir Orang Jelek Ini</b> {umention}")


async def block_user_func(client, message):
    user_id = await extract_user(message)
    tex = await message.reply("Processing...")
    if not user_id:
        return await tex.edit(f"Give a username to block.")
    if user_id == client.me.id:
        return await tex.edit("Ok done.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<b>Berhasil MemBlokir Jamet Kontol✌</b> {umention}")


async def setname(client, message):
    tex = await message.reply("Processing...")
    if len(message.command) == 1:
        return await tex.edit("Provide text to set as your name.")
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(
                f"<b>Successfully changed the name to</b> <code>{name}</code>"
            )
        except Exception as e:
            await tex.edit(f"<b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit("Provide text to set as your name.")


async def set_bio(client, message):
    tex = await message.reply("Processing...")
    if len(message.command) == 1:
        return await tex.edit("Provide text to set as bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"<b>Successfully changed bio to</b> <code>{bio}</code>")
        except Exception as e:
            await tex.edit(f"<b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit("Provide text to set as bio.")


async def list_admin(client, message):
    bacot = await message.reply("`Processing...`")
    a_chats = []
    me = await client.get_me()
    async for dialog in client.get_dialogs(limit=None):
        if dialog.chat.type == enums.ChatType.SUPERGROUP:
            gua = await dialog.chat.get_member(int(me.id))
            if gua.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chats.append(dialog.chat)
                
    text = ""
    j = 0
    for chat in a_chats:
        try:
            title = chat.title
        except Exception:
            title = "Private Group"
        if chat.username:
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{chat.username})[`{chat.id}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{chat.id}`]\n"
        j += 1
    
    if not text:
        await bacot.edit_text("Kamu tidak menjadi admin di grup manapun.")
    elif len(text) > 4096:
        with BytesIO(str.encode(text)) as out_file:
            out_file.name = "adminlist.text"
            await message.reply_document(
                document=out_file,
                disable_notification=True,
                quote=True,
            )
            await bacot.delete()
    else:
        await bacot.edit_text(
            f"**Kamu admin di `{len(a_chats)}` group:\n\n{text}**",
            disable_web_page_preview=True,
        )

async def set_pfp(client, message):
    po = "storage/TM_BLACK.png"
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=po)
        await client.set_profile_photo(photo=po)
        if os.path.exists(po):
            os.remove(po)
        await message.reply("**Foto Profil anda Berhasil Diubah.**")
    else:
        await message.reply(
            "`Balas ke foto apa pun untuk dipasang sebagai foto profile`"
        )
        await sleep(3)
        await message.delete()
