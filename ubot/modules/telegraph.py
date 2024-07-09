from ubot import *

__MODULE__ = "Telegraph"
__HELP__ = """
Bantuan Untuk Telegraph

• Perintah: <code>{0}tg</code> [reply media/text]
• Penjelasan: Untuk mengapload media/text ke telegra.ph.
"""


@PY.UBOT("tg")
async def _(client, message):
    await tg_cmd(client, message)
