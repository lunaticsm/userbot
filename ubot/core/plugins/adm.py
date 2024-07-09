import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *


from ubot import *

BANNED_USERS = filters.user()

async def admin_bannen(client, message):
    if message.command[0] == "kick":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("Tidak dapat menemukan pengguna.")
        if user_id == (await client.get_me()).id:
            return await message.reply_text(
                "Tidak bisa menendang diri sendiri."
            )
        if user_id == OWNER_ID:
            return await message.reply_text("Dia owner bot anda.")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                "Tidak bisa menendang admin."
            )
        mention = (await client.get_users(user_id)).mention
        await message.reply_to_message.delete()
        msg = f"<b>Kicked User :</b> {mention}\n<b>Admin :</b> {message.from_user.mention}"
        if reason:
            msg += f"\n<b>Reason :</b> {reason}"
        try:
            await message.chat.ban_member(user_id)
            await message.reply(msg)
            await asyncio.sleep(1)
            await message.chat.unban_member(user_id)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "ban":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("Tidak dapat menemukan pengguna.")
        if user_id == (await client.get_me()).id:
            return await message.reply_text(
                "Tidak bisa memblokir diri sendiri."
            )
        if user_id == OWNER_ID:
            return await message.reply_text("Dia adalah Owner Bot anda.")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                "Tidak dapat memblokir sesama admin."
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except IndexError:
            mention = (
                message.reply_to_message.sender_chat.title 
                if message.reply_to_message
                else "Anon")
        await message.reply_to_message.delete()
        msg = (
            f"<b>Banned Users :</b> {mention}\n<b>Admin :</b> {message.from_user.mention}"
        )
        if reason:
            msg += f"\n<b>Reason :</b> {reason}"
        try:
            await message.chat.ban_member(user_id)
            await message.reply(msg)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "mute":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("Tidak dapat menemukan pengguna.")
        if user_id == (await client.get_me()).id:
            return await message.reply_text(
                "Tidak dapat membisukan diri sendiri."
            )
        if user_id == OWNER_ID:
            return await message.reply_text("Dia Owner Bot Anda.")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                "Tidak bisa membisukan sesama admin."
            )
        mention = (await client.get_users(user_id)).mention
        await message.reply_to_message.delete()
        msg = f"<b>Muted Users :</b> {mention}\n<b>Admin :</b> {message.from_user.mention}"
        if reason:
            msg += f"\n<b>Reason :</b> {reason}"
        try:
            await message.chat.restrict_member(user_id, ChatPermissions())
            await message.reply(msg)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unmute":
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text("Tidak dapat menemukan pengguna.")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        try:
            await message.chat.unban_member(user_id)
            await message.reply(f"<b>{mention} sudah tidak bisu.</b>")
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unban":
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text("Tidak dapat menemukan pengguna.")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        try:
            await message.chat.unban_member(user_id)
            await message.reply(f"<b>{mention} sudah dapat bergabung.</b>")
        except Exception as error:
            await message.reply(error)



async def global_banned(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<code>Processing....</code>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await Tm.edit(
            "Gunakan format: <code>gban</code> [user_id/username/balas ke user]"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await Tm.edit("Tidak dapat menemukan user tersebut.")
        return
    iso = 0
    gagal = 0
    prik = user.id
    prok = await get_seles()
    gua = client.me.id
    udah = await is_banned_user(gua, prik)
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            
            if prik in DEVS:
                return await Tm.edit(
                    "Anda tidak bisa gban dia karena dia pembuat saya."
                )
            elif prik in prok:
                return await Tm.edit(
                    "Anda tidak bisa gban dia, karna dia adalah Admin Userbot Anda."
                )
            elif udah:
                return await Tm.edit(
                    "Pengguna ini sudah di gban."
                )
            elif prik not in prok and prik not in DEVS:
                try:
                    await add_banned_user(gua, prik)
                    await client.ban_chat_member(chat, prik)
                    iso = iso + 1
                    await asyncio.sleep(0.1)
                except BaseException:
                    gagal = gagal + 1
                    await asyncio.sleep(0.1)
    return await Tm.edit(
        f"""
<b>Global Banned</b>

<b>Berhasil Banned: {iso} Chat</b>
<b>Gagal Banned: {gagal} Chat</b>
<b>User: <a href='tg://user?id={prik}'>{user.first_name}</a></b>
"""
    )

async def cung_ban(client, message):
    user_id = await extract_user(message)
    if message.from_user.id != client.me.id:
        Tm = await message.reply("<code>Processing....</code>")
    else:
        Tm = await message.reply("<code>Processing....</code>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await Tm.edit(
            "Gunakan format: <code>ungban</code> [user_id/username/reply to user]"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await Tm.edit("Tidak menemukan user tersebut.")
        return
    iso = 0
    gagal = 0
    prik = user.id
    gua = client.me.id
    udah = await is_banned_user(gua, prik)
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            if prik in BANNED_USERS:
                BANNED_USERS.remove(prik) 
            try:
                await remove_banned_user(gua, prik)
                await client.unban_chat_member(chat, prik)
                iso = iso + 1
                await asyncio.sleep(0.1)
            except BaseException:
                gagal = gagal + 1
                await asyncio.sleep(0.1)

    return await Tm.edit(
        f"""
<b>Global Unbanned</b>

<b>Berhasil Unbanned: {iso} Chat</b>
<b>Gagal UnBanned: {gagal} Chat</b>
<b>User: <a href='tg://user?id={prik}'>{user.first_name}</a></b>
"""
    )


async def gbanlist(client, message):
    gua = client.me.id
    total = await get_banned_count(gua)
    if total == 0:
        return await message.reply("`Belum ada pengguna yang digban.`")
    nyet = await message.reply("`Processing...`")
    msg = "**Total Gbanned:** \n\n"
    tl = 0
    org = await get_banned_users(gua)
    for i in org:
        tl += 1
        try:
            user = await client.get_users(i)
            user = (
                user.first_name if not user.mention else user.mention
            )
            msg += f"{tl}• {user}\n"
        except Exception:
            msg += f"{tl}• {i}\n"
            continue
    if tl == 0:
        return await nyet.edit("`Belum ada pengguna yang digban.`")
    else:
        return await nyet.edit(msg)


async def pin_message(client, message):
    mmk = await message.reply("<code>Processing...</code>")
    if not message.reply_to_message:
        return await mmk.edit("Balas ke pesan untuk pin/unpin .")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await mmk.edit(
            f"<code>Unpinned [this]({r.link}) message.</code>",
            disable_web_page_preview=True,
        )
    try:
        await r.pin(disable_notification=True)
        await mmk.edit(
            f"<code>Pinned [this]({r.link}) message.</code>",
            disable_web_page_preview=True,
        )
    except ChatAdminRequired:
        return await mmk.edit("<b>Anda bukan admin di group ini !</b>")


async def promotte(client, message):
    user_id = await extract_user(message)
    biji = await message.reply("<code>Processing...</code>")
    if not user_id:
        return await biji.edit("Pengguna tidak ditemukan.")
    (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try:
        if message.command[0][0] == "full":
            await message.chat.promote_member(
                user_id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                ),
            )
            await asyncio.sleep(1)

            umention = (await client.get_users(user_id)).mention
            return await biji.edit(f"Fully Promoted! {umention}")

        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        await asyncio.sleep(1)

        umention = (await client.get_users(user_id)).mention
        await biji.edit(f"Promoted! {umention}")
    except ChatAdminRequired:
        return await biji.edit("<b>Anda bukan admin di group ini !</b>")



async def demote(client, message):
    user_id = await extract_user(message)
    sempak = await message.reply("<code>Processing...</code>")
    if not user_id:
        return await sempak.edit("Pengguna tidak ditemukan")
    if user_id == client.me.id:
        return await sempak.edit("Tidak bisa demote diri sendiri.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    await asyncio.sleep(1)

    umention = (await client.get_users(user_id)).mention
    await sempak.edit(f"Demoted! {umention}")