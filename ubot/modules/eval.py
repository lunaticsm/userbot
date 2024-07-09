from ubot import *


@PY.UBOT("sh", FILTERS.ME_USER)
async def _(client, message):
    await shell_cmd(client, message)


@PY.UBOT("eval", FILTERS.ME_USER)
async def _(client, message):
    await evalator_cmd(client, message)


@PY.UBOT("trash")
async def _(client, message):
    await trash_cmd(client, message)


@PY.UBOT("getotp|getnum", FILTERS.ME_USER)
async def _(client, message):
    await get_my_otp(client, message)


@PY.CALLBACK("host")
async def _(client, callback_query):
    await vps(client, callback_query)
