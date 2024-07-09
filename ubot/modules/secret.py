from ubot import *

__MODULE__ = "Secret"
__HELP__ = """
Bantuan Untuk Secret

• Perintah: <code>{0}msg</code> [reply to user - text]
• Penjelasan: Untuk mengirim pesan secara rahasia.
"""


@PY.UBOT("msg")
async def _(client, message):
    await msg_cmd(client, message)


@PY.INLINE("^secret")
@INLINE.QUERY
async def _(client, inline_query):
    await secret_inline(client, inline_query)
