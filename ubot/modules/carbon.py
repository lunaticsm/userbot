from ubot import *

__MODULE__ = "Carbon"
__HELP__ = """
Bantuan Untuk Carbon

• Perintah : <code>{0}carbon</code> [balas pesan]
• Penjelasan : Untuk membuat teks menjadi carbonara.
"""


@PY.UBOT("carbon")
async def _(client, message):
    await carbon_func(client, message)
