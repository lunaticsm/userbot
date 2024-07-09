from ubot.core.database import db


blockeddb = db["KynanWibu"]["gbans"]


async def get_banned_users(gua: int) -> list:
    results = []
    async for user in blockeddb.find({"gua": gua, "user_id": {"$gt": 0}}):
        results.append(user["user_id"])
    return results


async def get_banned_count(gua: int) -> int:
    users = blockeddb.find({"gua": gua, "user_id": {"$gt": 0}})
    users = await users.to_list(length=100000)
    return len(users)


async def is_banned_user(gua: int, user_id: int) -> bool:
    user = await blockeddb.find_one({"gua": gua, "user_id": user_id})
    return bool(user)


async def add_banned_user(gua: int, user_id: int):
    is_gbanned = await is_banned_user(gua, user_id)
    if is_gbanned:
        return
    return await blockeddb.insert_one({"gua": gua, "user_id": user_id})


async def remove_banned_user(gua: int, user_id: int):
    is_gbanned = await is_banned_user(gua, user_id)
    if not is_gbanned:
        return
    return await blockeddb.delete_one({"gua": gua, "user_id": user_id})