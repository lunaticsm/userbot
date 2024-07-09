from ubot.core.database import db

permitdb = db["KynanWibu"]["permitdb"]


async def add_approved_user(user_id):
    good_usr = int(user_id)
    does_they_exists = await permitdb.users.find_one({"user_id": "setujui"})
    if does_they_exists:
        await permitdb.users.update_one(
            {"user_id": "setujui"}, {"$push": {"good_id": good_usr}}
        )
    else:
        await permitdb.users.insert_one({"user_id": "setujui", "good_id": [good_usr]})


async def rm_approved_user(user_id):
    bad_usr = int(user_id)
    does_good_ones_exists = await permitdb.users.find_one({"user_id": "setujui"})
    if does_good_ones_exists:
        await permitdb.users.update_one(
            {"user_id": "setujui"}, {"$pull": {"good_id": bad_usr}}
        )
    else:
        return None


async def check_user_approved(user_id):
    random_usr = int(user_id)
    does_good_users_exists = await permitdb.users.find_one({"user_id": "setujui"})
    if does_good_users_exists:
        good_users_list = [
            cool_user for cool_user in does_good_users_exists.get("good_id")
        ]
        if random_usr in good_users_list:
            return True
        else:
            return False
    else:
        return False