from ubot.core.database import db


blchatdb = db["KynanWibu"]["blchat"]


async def get_chat(user_id):
    chat = await blchatdb.find_one({"chat": user_id})
    if not chat:
        return []
    return chat["list"]


async def add_chat(user_id, chat_id):
    list = await get_chat(user_id)
    list.append(chat_id)
    await blchatdb.update_one({"chat": user_id}, {"$set": {"list": list}}, upsert=True)
    return True


async def remove_chat(user_id, chat_id):
    list = await get_chat(user_id)
    list.remove(chat_id)
    await blchatdb.update_one({"chat": user_id}, {"$set": {"list": list}}, upsert=True)
    return True

async def blacklisted_chats(user_id: int) -> list:
    chats_list = []
    async for chat in blchatdb.users.find({"user_id": user_id, "chat_id": {"$lt": 0}}):
        chats_list.append(chat["chat_id"])
    return chats_list


async def blacklist_chat(user_id: int, chat_id: int) -> bool:
    if not await blchatdb.users.find_one({"user_id": user_id, "chat_id": chat_id}):
        await blchatdb.users.insert_one({"user_id": user_id, "chat_id": chat_id})
        return True
    return False


async def whitelist_chat(user_id: int, chat_id: int) -> bool:
    if await blchatdb.users.find_one({"user_id": user_id, "chat_id": chat_id}):
        await blchatdb.users.delete_one({"user_id": user_id, "chat_id": chat_id})
        return True
    return False
