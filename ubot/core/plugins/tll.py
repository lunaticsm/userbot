from asyncio import sleep

from ubot import *

spam_chats = []

stopProcess = False


async def mentionall(client: Client, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message.text
    if not direp:
        await message.reply("Silakan balas ke pesan !")
        return
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        elif usr.user.is_bot == True:
            pass
        elif usr.user.is_deleted == True:
            pass
        usrnum += 1
        usrtxt += f"**👤 [{usr.user.first_name}](tg://user?id={usr.user.id})**\n"
        if usrnum == 5:
            if direp:
                txt = f"**{direp}**\n\n{usrtxt}\n"
                await client.send_message(chat_id, txt)
            await sleep(2)
    try:
        spam_chats.remove(chat_id)
    except:
        pass



async def batal_tag(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("`Sepertinya tidak ada tagall disini.`")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("`Tag All Diberhentikan.`")
