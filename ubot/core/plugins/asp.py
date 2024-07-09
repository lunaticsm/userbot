import random

from pyrogram.enums import MessagesFilter

from ubot import *


async def video_asupan(client, message): 
     y = await message.reply_text("<b>🔍 Searching...</b>") 
     try: 
         asupannya = [] 
         async for asupan in client.search_messages( 
             "@arrasupantiktok", filter=MessagesFilter.VIDEO 
         ): 
             asupannya.append(asupan) 
         random_videos = random.sample(asupannya, min(5, len(asupannya)))
         for video in random_videos:
             await video.copy( 
                 message.chat.id, 
                 caption=f"", 
                 reply_to_message_id=message.id, 
             )
         await y.delete()
     except Exception as error: 
         await y.edit(error)


async def photo_cewek(client, message):
    y = await message.reply_text("<b>🔍 Mencari Cewe...</b>")
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@AyangSaiki", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(
            message.chat.id,
            caption=f"",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception as error:
        await y.edit(error)


async def photo_cowok(client, message):
    y = await message.reply_text("<b>🔍 Mencari Cowo...</b>")
    try:
        ayang2nya = []
        async for ayang2 in client.search_messages(
            "@Ayang2Saiki", filter=MessagesFilter.PHOTO
        ):
            ayang2nya.append(ayang2)
        photo = random.choice(ayang2nya)
        await photo.copy(
            message.chat.id,
            caption=f"",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception as error:
        await y.edit(error)


async def photo_anime(client, message):
    y = await message.reply_text("<b>🔍 Searching...</b>")
    anime_channel = random.choice(["@animehikarixa", "@Anime_WallpapersHD"])
    try:
        animenya = []
        async for anime in client.search_messages(
            anime_channel, filter=MessagesFilter.PHOTO
        ):
            animenya.append(anime)
        photo = random.choice(animenya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


async def video_bokep(client, message):
    y = await message.reply_text("<b>🔍 Searching...</b>")
    try:
        await client.join_chat("https://t.me/+kJJqN5kUQbs1NTVl")
    except:
        pass
    try:
        bokepnya = []
        async for bokep in client.search_messages(
            -1001867672427, filter=MessagesFilter.VIDEO
        ):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
    if client.me.id == OWNER_ID:
        return
    await client.leave_chat(-1001867672427)
