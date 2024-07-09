import asyncio
import os
import sys
import requests
import base64
from io import BytesIO

from PIL import Image
import importlib
import subprocess
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, errors, types
import traceback
    

files_cache = {}

async def render_message(app: Client, message: types.Message) -> dict:
    async def get_file(file_id) -> str:
        if file_id in files_cache:
            return files_cache[file_id]

        file_name = await app.download_media(file_id)
        with open(file_name, "rb") as f:
            content = f.read()
        os.remove(file_name)
        data = base64.b64encode(content).decode()
        files_cache[file_id] = data
        return data

    # text
    if message.photo:
        text = message.caption if message.caption else ""
    elif message.poll:
        text = get_poll_text(message.poll)
    elif message.sticker:
        text = ""
    else:
        text = get_reply_text(message)

    # media
    if message.photo:
        media = await get_file(message.photo.file_id)
    elif message.sticker:
        media = await get_file(message.sticker.file_id)
    else:
        media = ""

    # entities
    entities = []
    if message.entities:
        for entity in message.entities:
            entities.append(
                {
                    "offset": entity.offset,
                    "length": entity.length,
                    "type": entity.type,
                }
            )

    def move_forwards(msg: types.Message):
        if msg.forward_from:
            msg.from_user = msg.forward_from
        if msg.forward_sender_name:
            msg.from_user.id = 0
            msg.from_user.first_name = msg.forward_sender_name
            msg.from_user.last_name = ""
        if msg.forward_from_chat:
            msg.sender_chat = msg.forward_from_chat
            msg.from_user.id = 0
        if msg.forward_signature:
            msg.author_signature = msg.forward_signature

    move_forwards(message)

    # author
    author = {}
    if message.from_user and message.from_user.id != 0:
        from_user = message.from_user

        author["id"] = from_user.id
        author["name"] = get_full_name(from_user)
        if message.author_signature:
            author["rank"] = message.author_signature
        elif message.chat.type != "supergroup" or message.forward_date:
            author["rank"] = ""
        else:
            try:
                member = await message.chat.get_member(from_user.id)
            except errors.UserNotParticipant:
                author["rank"] = ""
            else:
                author["rank"] = getattr(member, "title", "") or (
                    "owner"
                    if member.status == "creator"
                    else "admin"
                    if member.status == "administrator"
                    else ""
                )

        if from_user.photo:
            author["avatar"] = await get_file(from_user.photo.big_file_id)
        elif not from_user.photo and from_user.username:
            # may be user blocked us, we will try to get avatar via t.me
            t_me_page = requests.get(f"https://t.me/{from_user.username}").text
            sub = '<meta property="og:image" content='
            index = t_me_page.find(sub)
            if index != -1:
                link = t_me_page[index + 35 :].split('"')
                if (
                    len(link) > 0
                    and link[0]
                    and link[0] != "https://telegram.org/img/t_logo.png"
                ):
                    # found valid link
                    avatar = requests.get(link[0]).content
                    author["avatar"] = base64.b64encode(avatar).decode()
                else:
                    author["avatar"] = ""
            else:
                author["avatar"] = ""
        else:
            author["avatar"] = ""
    elif message.from_user and message.from_user.id == 0:
        author["id"] = 0
        author["name"] = message.from_user.first_name
        author["rank"] = ""
    else:
        author["id"] = message.sender_chat.id
        author["name"] = message.sender_chat.title
        author["rank"] = "channel" if message.sender_chat.type == "channel" else ""

        if message.sender_chat.photo:
            author["avatar"] = await get_file(message.sender_chat.photo.big_file_id)
        else:
            author["avatar"] = ""
    author["via_bot"] = message.via_bot.username if message.via_bot else ""

    # reply
    reply = {}
    reply_msg = message.reply_to_message
    if reply_msg and not reply_msg.empty:
        move_forwards(reply_msg)

        if reply_msg.from_user:
            reply["id"] = reply_msg.from_user.id
            reply["name"] = get_full_name(reply_msg.from_user)
        else:
            reply["id"] = reply_msg.sender_chat.id
            reply["name"] = reply_msg.sender_chat.title

        reply["text"] = get_reply_text(reply_msg)

    return {
        "text": text,
        "media": media,
        "entities": entities,
        "author": author,
        "reply": reply,
    }


def get_audio_text(audio: types.Audio) -> str:
    if audio.title and audio.performer:
        return f" ({audio.title} — {audio.performer})"
    elif audio.title:
        return f" ({audio.title})"
    elif audio.performer:
        return f" ({audio.performer})"
    else:
        return ""


def get_reply_text(reply: types.Message) -> str:
    return (
        "📷 Photo" + ("\n" + reply.caption if reply.caption else "")
        if reply.photo
        else get_reply_poll_text(reply.poll)
        if reply.poll
        else "📍 Location"
        if reply.location or reply.venue
        else "👤 Contact"
        if reply.contact
        else "🖼 GIF"
        if reply.animation
        else "🎧 Music" + get_audio_text(reply.audio)
        if reply.audio
        else "📹 Video"
        if reply.video
        else "📹 Videomessage"
        if reply.video_note
        else "🎵 Voice"
        if reply.voice
        else (reply.sticker.emoji + " " if reply.sticker.emoji else "") + "Sticker"
        if reply.sticker
        else "💾 File " + reply.document.file_name
        if reply.document
        else "🎮 Game"
        if reply.game
        else "🎮 set new record"
        if reply.game_high_score
        else f"{reply.dice.emoji} - {reply.dice.value}"
        if reply.dice
        else (
            "👤 joined the group"
            if reply.new_chat_members[0].id == reply.from_user.id
            else "👤 invited %s to the group"
            % (get_full_name(reply.new_chat_members[0]))
        )
        if reply.new_chat_members
        else (
            "👤 left the group"
            if reply.left_chat_member.id == reply.from_user.id
            else "👤 removed %s" % (get_full_name(reply.left_chat_member))
        )
        if reply.left_chat_member
        else f"✏ changed group name to {reply.new_chat_title}"
        if reply.new_chat_title
        else "🖼 changed group photo"
        if reply.new_chat_photo
        else "🖼 removed group photo"
        if reply.delete_chat_photo
        else "📍 pinned message"
        if reply.pinned_message
        else "👥 created the group"
        if reply.group_chat_created or reply.supergroup_chat_created
        else "👥 created the channel"
        if reply.channel_chat_created
        else reply.text or "unsupported message"
    )


def get_poll_text(poll: types.Poll) -> str:
    text = get_reply_poll_text(poll) + "\n"

    text += poll.question + "\n"
    for option in poll.options:
        text += f"- {option.text}"
        if option.voter_count > 0:
            text += f" ({option.voter_count} voted)"
        text += "\n"

    text += f"Total: {poll.total_voter_count} voted"

    return text


def get_reply_poll_text(poll: types.Poll) -> str:
    if poll.is_anonymous:
        text = "📊 Anonymous poll" if poll.type == "regular" else "📊 Anonymous quiz"
    else:
        text = "📊 Poll" if poll.type == "regular" else "📊 Quiz"
    if poll.is_closed:
        text += " (closed)"

    return text


def get_full_name(user: types.User) -> str:
    name = user.first_name
    if user.last_name:
        name += " " + user.last_name
    return name


def resize_image(input_img, output=None, img_type="PNG"):
    if output is None:
        output = BytesIO()
        output.name = f"sticker.{img_type.lower()}"

    with Image.open(input_img) as img:
        # We used to use thumbnail(size) here, but it returns with a *max* dimension of 512,512
        # rather than making one side exactly 512 so we have to calculate dimensions manually :(
        if img.width == img.height:
            size = (512, 512)
        elif img.width < img.height:
            size = (max(512 * img.width // img.height, 1), 512)
        else:
            size = (512, max(512 * img.height // img.width, 1))

        img.resize(size).save(output, img_type)

    return output
