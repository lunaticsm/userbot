import asyncio

from pyrogram.enums import ChatType

from ubot import OWNER_ID, bot, ubot


async def install_my_peer(client):
    users = []
    groups = []
    async for dialog in client.get_dialogs(limit=None):
        if dialog.chat.type == ChatType.PRIVATE:
            users.append(dialog.chat.id)
            await asyncio.sleep(1)
        elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            groups.append(dialog.chat.id)
            await asyncio.sleep(1)
        client._get_my_peer[client.me.id] = {"pm": users, "gc": groups}
  

async def installPeer():
    tasks = [install_my_peer(client) for client in ubot._ubot]
    await asyncio.gather(*tasks, return_exceptions=True)
    await bot.send_message(OWNER_ID, "✅ Berhasil Menginstall Data Pengguna")
