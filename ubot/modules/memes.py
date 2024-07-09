from ubot import *

__MODULE__ = "Meme"
__HELP__ = """
 Bantuan Untuk Meme

• Perintah : <code>{0}memes</code> [teks]
• Penjelasan : Untuk membuat kata memes random.
"""


@PY.UBOT("mms|memes")
async def _(client, message):
    await memes_cmd(client, message)
