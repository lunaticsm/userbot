import asyncio
import os
import requests

from pyrogram import *
from pyrogram.types import *
from base64 import b64decode
from io import BytesIO

from ubot.core.helpers.quote import render_message, resize_image
from pyrogram.raw.functions.messages import DeleteHistory


async def quotly_cmd(client, message):
    info = await message.reply("<b>Processing...</b>", quote=True)
    await client.unblock_user("@QuotLyBot")
    if message.reply_to_message:
        if len(message.command) < 2:
            msg = [message.reply_to_message]
        else:
            try:
                count = int(message.command[1])
            except Exception as error:
                await info.edit(error)
            msg = [
                i
                for i in await client.get_messages(
                    chat_id=message.chat.id,
                    message_ids=range(
                        message.reply_to_message.id, message.reply_to_message.id + count
                    ),
                    replies=-1,
                )
            ]
        try:
            for x in msg:
                await x.forward("@QuotLyBot")
        except Exception:
            pass
        await asyncio.sleep(9)
        await info.delete()
        async for quotly in client.get_chat_history("@QuotLyBot", limit=1):
            if not quotly.sticker:
                await message.reply(
                    f"❌ @QuotLyBot Error", quote=True
                )
            else:
                sticker = await client.download_media(quotly)
                await message.reply_sticker(sticker, quote=True)
                os.remove(sticker)
    else:
        if len(message.command) < 2:
            return await info.edit("<code>Balas ke pesan</code>")
        else:
            msg = await client.send_message(
                "@QuotLyBot", f"/qcolor {message.command[1]}"
            )
            await asyncio.sleep(1)
            get = await client.get_messages("@QuotLyBot", msg.id + 1)
            await info.edit(
                f"<b>Warna latar belakang di ganti ke :</b> <code>{get.text.split(':')[1]}</code>"
            )
    user_info = await client.resolve_peer("@QuotLyBot")
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))


async def fake_quote_cmd(client: Client, message: Message):
    send_for_me = "!me" in message.command or "!ls" in message.command

    if len(message.command) < 3:
        return await message.edit("{message.text} <username> <message>")

    target_user = message.command[1]
    if not target_user.startswith("@"):
        return await message.edit("Invalid username format.")
    target_user = target_user[1:]

    try:
        user = await client.get_users(target_user)
    except errors.exceptions.bad_request_400.UsernameNotOccupied:
        return await message.edit("Not found a username.")
    except IndexError:
        return await message.edit("Only for user.")

    fake_quote_text = " ".join(message.command[2:])

    if not fake_quote_text:
        return await message.edit("Empty message.")

    q_message = await client.get_messages(message.chat.id, message.id)
    q_message.text = fake_quote_text
    q_message.entities = None

    q_message.from_user.id = user.id
    q_message.from_user.first_name = user.first_name
    q_message.from_user.last_name = user.last_name
    q_message.from_user.username = user.username
    q_message.from_user.photo = user.photo

    if send_for_me:
        await message.delete()
        message = await client.send_message("me", "Processing...")
    else:
        await message.edit("Loading...")

    url = "https://quotes.fl1yd.su/generate"
    params = {
        "messages": [await render_message(client, q_message)],
        "quote_color": "#162330",
        "text_color": "#fff",
    }

    response = requests.post(url, json=params)
    if not response.ok:
        return await message.edit(
            f"<b>Error!</b>\n" f"<code>{response.text}</code>"
        )

    resized = resize_image(
        BytesIO(response.content), img_type="webp"
    )
    await message.edit("Sending...")

    try:
        func = client.send_sticker
        chat_id = "me" if send_for_me else message.chat.id
        await func(chat_id, resized)
    except errors.RPCError as e:
        await message.edit(e)
    else:
        await message.delete()
