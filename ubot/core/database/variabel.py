from ubot.core.database import db

vardb = db["KynanWibu"]["variable"]

async def set_var(user_id, var, value):
    vari = await vardb.find_one({"user_id": user_id, "var": var})
    if vari:
        await vardb.update_one(
            {"user_id": user_id, "var": var}, {"$set": {"vardb": value}}
        )
    else:
        await vardb.insert_one({"user_id": user_id, "var": var, "vardb": value})


async def get_var(user_id, var):
    cosvar = await vardb.find_one({"user_id": user_id, "var": var})
    if not cosvar:
        return None
    else:
        get_cosvar = cosvar["vardb"]
        return get_cosvar


async def del_var(user_id, var):
    cosvar = await vardb.find_one({"user_id": user_id, "var": var})
    if cosvar:
        await vardb.delete_one({"user_id": user_id, "var": var})
        return True
    else:
        return False