import asyncio
import os

from pyrogram.enums import MessageMediaType, MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto

from ubot import *


async def convert_anime(client, message):
    Tm = await message.reply("<b>Tunggu Sebentar......</b>")
    if message.reply_to_message:
        if len(message.command) < 2:
            if message.reply_to_message.photo:
                file = "foto"
                get_photo = message.reply_to_message.photo.file_id
            elif message.reply_to_message.sticker:
                file = "sticker"
                get_photo = await dl_pic(client, message.reply_to_message)
            elif message.reply_to_message.animation:
                file = "gift"
                get_photo = await dl_pic(client, message.reply_to_message)
            else:
                return await Tm.edit(
                    "<b>Silakan balas ke</b> <code>photo/stiker</code>"
                )
        else:
            if message.command[1] in ["foto", "profil", "photo"]:
                chat = (
                    message.reply_to_message.from_user
                    or message.reply_to_message.sender_chat
                )
                file = "foto profil"
                get = await client.get_chat(chat.id)
                photo = get.photo.big_file_id
                get_photo = await dl_pic(client, photo)
    else:
        if len(message.command) < 2:
            return await Tm.edit(
                "Silakan balas ke foto"
            )
        else:
            try:
                file = "foto"
                get = await client.get_chat(message.command[1])
                photo = get.photo.big_file_id
                get_photo = await dl_pic(client, photo)
            except Exception as error:
                return await Tm.edit(error)
    await Tm.edit("<b>Processing...</b>")
    await client.unblock_user("@qq_neural_anime_bot")
    send_photo = await client.send_photo("@qq_neural_anime_bot", get_photo)
    await asyncio.sleep(30)
    await send_photo.delete()
    await Tm.delete()
    info = await client.resolve_peer("@qq_neural_anime_bot")
    anime_photo = []
    async for anime in client.search_messages(
        "@qq_neural_anime_bot", filter=MessagesFilter.PHOTO
    ):
        anime_photo.append(
            InputMediaPhoto(
                anime.photo.file_id, caption=f"<b>Edited By : {bot.me.mention}</b>"
            )
        )
    if anime_photo:
        await client.send_media_group(
            message.chat.id,
            anime_photo,
            reply_to_message_id=message.id,
        )
        return await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))

    else:
        await client.send_message(
            message.chat.id,
            f"<b>Gagal merubah gambar {file}.</b>",
            reply_to_message_id=message.id,
        )
        return await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))


async def convert_photo(client, message):
    try:
        Tm = await message.reply("Downloading...")
        file_io = await dl_pic(client, message.reply_to_message)
        file_io.name = "sticker.png"
        await client.send_photo(
            message.chat.id,
            file_io,
            reply_to_message_id=message.id,
        )
        await Tm.delete()
    except Exception as e:
        await Tm.delete()
        return await client.send_message(
            message.chat.id,
            e,
            reply_to_message_id=message.id,
        )


async def convert_sticker(client, message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            return await message.reply_text("Silakan balas ke stiker")
        sticker = await client.download_media(
            message.reply_to_message.photo.file_id,
            f"sticker_{message.from_user.id}.webp",
        )
        await message.reply_sticker(sticker)
        os.remove(sticker)
    except Exception as e:
        await message.reply_text(str(e))


async def convert_gif(client, message):
    TM = await message.reply("<b>Processing...</b>")
    if not message.reply_to_message.sticker:
        return await TM.edit("<b>Silakan balas ke stiker.</b>")
    await TM.edit("<b>Downloading...</b>")
    file = await client.download_media(
        message.reply_to_message,
        f"Gift_{message.from_user.id}.mp4",
    )
    try:
        await client.send_animation(
            message.chat.id, file, reply_to_message_id=message.id
        )
        os.remove(file)
        await TM.delete()
    except Exception as error:
        await TM.edit(error)


async def convert_audio(client, message):
    replied = message.reply_to_message
    Tm = await message.reply("<b>Tunggu Sebentar...</b>")
    if not replied:
        return await Tm.edit("<b>Silakan balas ke video.</b>")
    if replied.media == MessageMediaType.VIDEO:
        await Tm.edit("<b>Downloading...</b>")
        file = await client.download_media(
            message=replied,
            file_name=f"toaudio_{replied.id}",
        )
        out_file = f"{file}.mp3"
        try:
            await Tm.edit("<b>Processing...</b>")
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {out_file}"
            await run_cmd(cmd)
            await Tm.edit("<b>Uploading...</b>")
            await client.send_voice(
                message.chat.id,
                voice=out_file,
                reply_to_message_id=message.id,
            )
            os.remove(file)
            await Tm.delete()
        except Exception as error:
            await Tm.edit(error)
    else:
        return await Tm.edit("<b>Silakan balas video</b>")


async def convert_efek(client, message):
    helo = get_arg(message)
    rep = message.reply_to_message
    if rep and helo:
        tau = ["bengek", "robot", "jedug", "fast", "echo"]
        if helo in tau:
            Tm = await message.reply(f"Proses merubah suara menjadi : {helo}")
            indir = await client.download_media(rep)
            KOMUT = {
                "bengek": '-filter_complex "rubberband=pitch=1.5"',
                "robot": "-filter_complex \"afftfilt=real='hypot(re,im)*sin(0)':imag='hypot(re,im)*cos(0)':win_size=512:overlap=0.75\"",
                "jedug": '-filter_complex "acrusher=level_in=8:level_out=18:bits=8:mode=log:aa=1"',
                "fast": "-filter_complex \"afftfilt=real='hypot(re,im)*cos((random(0)*2-1)*2*3.14)':imag='hypot(re,im)*sin((random(1)*2-1)*2*3.14)':win_size=128:overlap=0.8\"",
                "echo": '-filter_complex "aecho=0.8:0.9:500|1000:0.2|0.1"',
            }
            ses = await asyncio.create_subprocess_shell(
                f"ffmpeg -i '{indir}' {KOMUT[helo]} audio.mp3"
            )
            await ses.communicate()
            await Tm.delete()
            await rep.reply_voice("audio.mp3", caption=f"Efek {helo}")
            os.remove("audio.mp3")
        else:
            await message.reply(f"Silakan masukkan efek : {tau}")
    else:
        await Tm.edit(
            f"Silakan balas audio.\n\nContoh : <code>{0}efek bengek</code>[balas audio]"
        )
