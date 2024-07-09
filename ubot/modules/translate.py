from ubot import *

__MODULE__ = "Translate"
__HELP__ = """
Bantuan Untuk Translate

• Perintah: <code>{0}tr</code> [reply/text]
• Penjelasan: Untuk menerjemahkan text dengan kode negara yang diinginkan.

• Perintah: <code>{0}set_lang</code>
• Penjelasan: Untuk mengubah bahasa.

• Perintah: <code>{0}tts</code> [reply/text]
• Penjelasan: Untuk menerjemahkan text dengan kode negara yang diinginkan serta merubahnya menjadi pesan suara.
"""


@PY.UBOT("tts")
async def _(client, message):
    await tts_cmd(client, message)


@PY.UBOT("tr|tl")
async def _(client, message):
    await tr_cmd(client, message)


@PY.UBOT("set_lang")
async def _(client, message):
    await set_lang_cmd(client, message)


@PY.INLINE("^ubah_bahasa")
@INLINE.QUERY
async def _(client, inline_query):
    await ubah_bahasa_inline(client, inline_query)


@PY.CALLBACK("^set_bahasa")
@INLINE.DATA
async def _(client, callback_query):
    await set_bahasa_callback(client, callback_query)
