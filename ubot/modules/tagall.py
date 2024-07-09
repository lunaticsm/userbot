from ubot import *

__MODULE__ = "Mention"
__HELP__ = """
Bantuan Untuk Mention

• Perintah: <code>{0}all</code> [type message/reply message]
• Penjelasan: Untuk memention semua anggota grup dengan pesan yang anda inginkan.

• Perintah: <code>{0}batal</code>
• Penjelasan: Untuk membatalkan memention anggota grup.
"""



@PY.UBOT("all")
async def _(client, message):
    await mentionall(client, message)

@PY.UBOT("batal")
async def _(client, message):
    await batal_tag(client, message)

