from ubot import *

__MODULE__ = "Button"
__HELP__ = """
 Bantuan Untuk Button

• Perintah : <code>{0}button</code> Teks ~ Button Teks|Button Link.
• Penjelasan : Untuk membuat teks menjadi button.

• Contoh : Google ~ Klik Disini|google.com
"""


@PY.UBOT("button")
async def _(client, message):
    await cmd_button(client, message)


@PY.INLINE("^get_button")
@INLINE.QUERY
async def _(client, inline_query):
    await inline_button(client, inline_query)
