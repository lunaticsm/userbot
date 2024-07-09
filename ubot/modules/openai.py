from ubot import *

__MODULE__ = "OpenAi"
__HELP__ = """
 Bantuan Untuk OpenAi

• Perintah : <code>{0}ai</code> ᴏʀ <code>{0}ask</code>  [query]
• Penjelasan : Untuk menggunakan chatgpt.

• Perintah : <code>{0}dalle</code> ᴏʀ <code>{0}photo</code> [query]
• Penjelasan : Untuk membuat sebuah foto.

• Perintah : <code>{0}stt</code> [balas audio]
• Penjelasan : Untuk merubah pesan suara ke teks.
"""


@PY.UBOT("ai|ask")
async def _(client, message):
    await ai_cmd(client, message)


@PY.UBOT("dalle|photo")
async def _(client, message):
    await dalle_cmd(client, message)


@PY.UBOT("stt")
async def _(client, message):
    await stt_cmd(client, message)
