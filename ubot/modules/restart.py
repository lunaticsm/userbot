from ubot import *


@PY.BOT("login", FILTERS.ME_USER)
@PY.UBOT("login", FILTERS.ME_USER)
async def _(client, message):
    await login_cmd(client, message)


@PY.BOT("restart")
async def _(client, message):
    await restart_cmd2(client, message)
