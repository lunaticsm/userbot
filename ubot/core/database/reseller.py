from ubot.core.database import db

resell = db["KynanWibu"]["babu"]


async def get_seles():
    seles = await resell.find_one({"babu": "babu"})
    if not seles:
        return []
    return seles["reseller"]


async def add_seles(user_id):
    reseller = await get_seles()
    reseller.append(user_id)
    await resell.update_one(
        {"babu": "babu"}, {"$set": {"reseller": reseller}}, upsert=True
    )
    return True


async def remove_seles(user_id):
    reseller = await get_seles()
    reseller.remove(user_id)
    await resell.update_one(
        {"babu": "babu"}, {"$set": {"reseller": reseller}}, upsert=True
    )
    return True
