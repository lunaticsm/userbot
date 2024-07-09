from ubot import *

__MODULE__ = "Memify"
__HELP__ = """
 Bantuan Untuk Memify

• Perintah : <code>{0}mmf</code> [teks]
• Penjelasan : Untuk membuat gambar menjadi kecil.
"""


@PY.UBOT("mmf|memify")
async def _(client, message):
    await memify_cmd(client, message)
