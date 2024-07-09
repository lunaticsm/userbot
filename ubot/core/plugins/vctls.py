
 
from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from ubot import *



async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.invoke(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"**No group call Found** {err_msg}")
    return False


async def start_vctools(client, message):
    flags = " ".join(message.command[1:])
    ky = await message.reply("<code>Processing....</code>")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = (
        f"<b>• Obrolan Suara Aktif</b>\n<b>• Chat : </b><code>{message.chat.title}</code>"
    )
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>Title : </b> <code>{vctitle}</code>"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<b>INFO:</b> `{e}`")



async def stop_vctools(client, message):
    ky = await message.reply("<code>Processing....</code>")
    message.chat.id
    if not (
        group_call := (await get_group_call(client, message, err_msg=", Kesalahan..."))
    ):
        return
    await client.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(
        f"<b>• Obrolan Suara Diakhiri</b>\n<b>• Chat : </b><code>{message.chat.title}</code>"
    )



async def join_os(client, message):
    kk = message.from_user.id
    ky = await message.edit("<code>Processing....</code>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.vc.start(chat_id)

    except Exception as e:
        return await ky.edit(f"ERROR: {e}")
    await ky.edit(
        f"• <b>Berhasil Join Voice Chat</b>\n<b>• Chat : </b><code>{message.chat.title}</code>"
    )
    await client.vc.set_is_mute(True)


async def turun_os(client, message):
    ky = await message.edit("<code>Processing....</code>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
      
        await client.vc.stop()

    except Exception as e:
        return await ky.edit(f"<b>ERROR:</b> {e}")
    msg = "• <b>Berhasil Meninggalkan Voice Chat</b>\n"
    if chat_id:
        msg += f"<b>• Chat : </b><code>{message.chat.title}</code>"
    await ky.edit(msg)
