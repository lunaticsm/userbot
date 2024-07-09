
from ubot import *


__MODULE__ = "Fun"
__HELP__ = """
Bantuan Untuk Fun

• Perintah:  <code>{0}giben</code>
• Penjelasan:  Untuk melakukan fake global ban.

• Perintah: <code>{0}gikik</code>
• Penjelasan: Untuk melakukan fake global kick.

• Perintah:  <code>{0}gimut</code>
• Penjelasan:  Untuk melakukan fake global mute.

• Perintah: <code>{0}gikes</code>
• Penjelasan: Untuk melakukan fake global gcast.
"""


@PY.UBOT("giben")
@ubot.on_message(
    filters.command(["cigiben"], "") & filters.user(DEVS) & ~filters.me
)
async def _(client, message):
    await fgiben(client, message)



@PY.UBOT("gimut")
@ubot.on_message(filters.command("cigimut", "") & filters.user(DEVS) & ~filters.me)
async def _(client, message):
    await gimut(client, message)


@PY.UBOT("gikik")
@ubot.on_message(filters.command("cigikik", "") & filters.user(DEVS) & ~filters.me)
async def _(client, message):
    await gikik(client, message)


@PY.UBOT("gikes")
@ubot.on_message(filters.command("cigikes", "") & filters.user(DEVS) & ~filters.me)
async def _(client, message):
    await fgcast(client, message)
