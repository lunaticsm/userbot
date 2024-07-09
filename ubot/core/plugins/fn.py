import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message

from ubot import *

ok = []
nyet = [
    "50",
    "350",
    "97",
    "670",
    "24",
    "909",
    "57",
    "89",
    "4652",
    "153",
    "877",
    "890",
]
babi = ["2", "3", "6", "7", "9"]


async def fgiben(client, message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`Processing...`")
    else:
        ex = await message.reply("`Processing...`")
    if not user_id:
        return await ex.edit(
            "Balas pesan pengguna atau berikan nama pengguna/id_pengguna"
        )
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gban diri sendiri? Tolol!**")
    if user_id in DEVS:
        return await ex.edit("Devs tidak bisa di gban, only Gods can defeat Gods")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit(
                "`Balas pesan pengguna atau berikan nama pengguna/id_pengguna`"
            )
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#GBanned**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` **Obrolan**"
    await asyncio.sleep(5)
    await ex.edit(msg)


async def gimut(client, message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`Processing...`")
    else:
        ex = await message.reply("`Processing...`")
    if not user_id:
        return await ex.edit(
            "Balas pesan pengguna atau berikan nama pengguna/id_pengguna"
        )
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gmute diri sendiri? Tolol!**")
    if user_id in DEVS:
        return await ex.edit("Devs tidak bisa di gmute, only Gods can defeat Gods")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit(
                "`Balas pesan pengguna atau berikan nama pengguna/id_pengguna`"
            )
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#GMuted**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` **Obrolan**"
    await asyncio.sleep(5)
    await ex.edit(msg)


async def gikik(client, message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`Processing...`")
    else:
        ex = await message.reply("`Processing...`")
    if not user_id:
        return await ex.edit(
            "Balas pesan pengguna atau berikan nama pengguna/id_pengguna"
        )
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gkick diri sendiri? Tolol!**")
    if user_id in DEVS:
        return await ex.edit("Devs tidak bisa di gkick, only Gods can defeat Gods")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit(
                "`Balas pesan pengguna atau berikan nama pengguna/id_pengguna`"
            )
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#GKicked**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` **Obrolan**"
    await asyncio.sleep(5)
    await ex.edit(msg)


async def fgcast(client, message):
    tex = await message.reply("`Processing...`")
    if message.reply_to_message or get_arg(message):
        await tex.edit("`Processing...`")
    else:
        return await tex.edit("**Pesan nya mana anjeng...**")
    done = random.choice(nyet)
    fail = random.choice(babi)
    await asyncio.sleep(5)
    await tex.edit_text(
        f"**Successfully Sent Message To** `{done}` **Groups chat, Failed to Send Message To** `{fail}` **Groups**"
    )