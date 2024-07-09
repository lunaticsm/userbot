from ubot.core.database import db

getopt = db["KynanWibu"]["twofactor"]


async def get_two_factor(user_id):
    user = await getopt.users.find_one({"_id": user_id})
    if user:
        return user.get("twofactor")
    else:
        return None


async def set_two_factor(user_id, twofactor):
    await getopt.users.update_one(
        {"_id": user_id}, {"$set": {"twofactor": twofactor}}, upsert=True
    )


async def rem_two_factor(user_id):
    await getopt.users.update_one(
        {"_id": user_id}, {"$unset": {"twofactor": ""}}, upsert=True
    )
