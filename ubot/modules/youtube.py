from ubot import *

__MODULE__ = "Youtube"
__HELP__ = """
Bantuan Untuk Youtube

• Perintah: <code>{0}song</code> [song title]
• Penjelasan: Untuk mendownload music yang diinginkan.

• Perintah: <code>{0}vsong</code> [video title]
• Penjelasan: Untuk mendownload video yang diinginkan.
"""


@PY.UBOT("vsong")
async def _(client, message):
    await vsong_cmd(client, message)


@PY.UBOT("song")
async def _(client, message):
    await song_cmd(client, message)
