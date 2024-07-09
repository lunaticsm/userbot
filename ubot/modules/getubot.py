from ubot import *


@PY.UBOT("getubot", FILTERS.ME_USER)
async def _(client, message):
    await getubot_cmd(client, message)

@PY.INLINE("^ambil_ubot")
async def _(client, inline_query):
    await getubot_query(client, inline_query)

@PY.CALLBACK("close_user")
async def _(client, callback_query):
    await close_usernya(client, callback_query)
