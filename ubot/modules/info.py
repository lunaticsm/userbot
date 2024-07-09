from ubot import *

__MODULE__ = "Info"
__HELP__ = """
 Bantuan Untuk Info

• Perintah : <code>{0}info</code> [user_id/username/balas pesan]
• Penjelasan : Untuk melihat informasi pengguna.

• Perintah : <code>{0}cinfo</code> [user_id/username/balas pesan]
• Penjelasan : Untuk melihat informasi obrolan.
"""


@PY.UBOT("whois|info")
async def _(client, message):
    await info_cmd(client, message)


@PY.UBOT("cwhois|cinfo")
async def _(client, message):
    await cinfo_cmd(client, message)
