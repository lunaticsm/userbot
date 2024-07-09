from ubot import *

__MODULE__ = "Nulis"
__HELP__ = """
 Bantuan Untuk Nulis

• Perintah : <code>{0}nulis</code> [teks/balas pesan]
• Penjelasan : Untuk menulis sesuatu dikertas.
"""


@PY.UBOT("nulis")
async def _(client, message):
    await nulis_cmd(client, message)
