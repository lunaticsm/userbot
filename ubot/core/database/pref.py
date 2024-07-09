from ubot.core.database import db

prefixes = db["KynanWibu"]["prefixesi"]

async def get_pref(user_id):
    user = await prefixes.users.find_one({"_id": user_id})
    if user:
        return user.get("prefixesi")
    else:
        return "."

async def set_pref(user_id, prefix):
    await prefixes.users.update_one(
        {"_id": user_id}, {"$set": {"prefixesi": prefix}}, upsert=True
    )


async def rem_pref(user_id):
    await prefixes.users.update_one(
        {"_id": user_id}, {"$unset": {"prefixesi": ""}}, upsert=True
    )