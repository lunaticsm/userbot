from ubot import *


@PY.UBOT("catur")
async def _(client, message):
    await catur_cmd(client, message)
