from pyrogram import Client, enums, filters
from pyrogram.types import Message

from ubot import *


async def join(client, message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply("Processing...")
    try:
        await xxnx.edit(f"Berhasil bergabung ke : `{Man}`")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"ERROR: \n\n{str(ex)}")


async def leave(client, message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply("Processing...")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit("Dilarang menggunakan perintah ini disni .")
    try:
        await xxnx.edit_text(f"{client.me.first_name} Aku depresi .")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"ERROR: \n\n{str(ex)}")


async def kickmeall(client, message):
    Man = await message.reply("Proses Pengeluaran Global Grup...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"Berhasil keluar dari {done} grup, Gagal keluar dari {er} grup."
    )


async def kickmeallch(client, message):
    Man = await message.reply("Proses Pengeluaran Global Channel...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"Berhasil keluar dari {done} channel, Gagal keluar dari {er} channel."
    )
