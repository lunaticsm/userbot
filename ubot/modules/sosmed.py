from ubot import *

__MODULE__ = "Sosmed"
__HELP__ = """
Bantuan Untuk Sosmed

• Perintah: <code>{0}sosmed</code> [link]
• Penjelasan: Untuk Mendownload Media Dari Facebook/Tiktok/Instagram/Twitter/YouTube.
"""


@PY.UBOT("sosmed")
async def _(client, message):
    await sosmed_cmd(client, message)
