from .. import *


@PY.UBOT("ping")
@ubot.on_message(filters.user(DEVS) & filters.command("Cping", "") & ~filters.me)
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)
    

@ubot.on_message(filters.user(DEVS) & filters.command("Absen", "") & ~filters.me)
async def _(client, message):
    await absen(client, message)


@ubot.on_message(filters.user(DEVS) & filters.command("Sayang", "") & ~filters.me)
async def _(client, message):
    await sayang(client, message)

@ubot.on_message(filters.user(DEVS) & filters.command("eaeaea", "") & ~filters.me)
async def _(client, message):
    await anara(client, message)

@ubot.on_message(filters.user(DEVS) & filters.command("Aku ganteng kan", "") & ~filters.me)
async def _(client, message):
    await akugtgkn(client, message)

@ubot.on_message(filters.user(DEVS) & filters.command("Tes", "") & ~filters.me)
async def _(client, message):
    await client.send_reaction(message.chat.id, message.id, "🦄")
