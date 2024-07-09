from ubot import *

__MODULE__ = "Blacklist"
__HELP__ = """
 Bantuan Untuk Blacklist

• Perintah : <code>{0}rallbl</code>
• Penjelasan : Menghapus semua anti gcast

• Perintah : <code>{0}addbl</code>
• Penjelasan : Menambahkan grup kedalam anti Gcast.

• Perintah : <code>{0}unbl</code>
• Penjelasan : Menghapus grup dari daftar anti Gcast.

• Perintah : <code>{0}listbl</code>
• Penjelasan : Melihat daftar grup anti Gcast.
"""


@PY.UBOT("addbl", FILTERS.ME_GROUP)
async def _(client, message):
    await add_blaclist(client, message)


@PY.UBOT("unbl", FILTERS.ME_GROUP)
async def _(client, message):
    await del_blacklist(client, message)


@PY.UBOT("rallbl")
async def _(client, message):
    await rem_all_blacklist(client, message)


@PY.UBOT("listbl")
async def _(client, message):
    await get_blacklist(client, message)
