from ubot import *

__MODULE__ = "Join"
__HELP__ = """
 Bantuan Untuk Join

• Perintah : <code>{0}kickme</code>
• Penjelasan : Untuk keluar dari grup.

• Perintah : <code>{0}join</code> [username]
• Penjelasan : Untuk bergabung ke grup dengan username.

• Perintah : <code>{0}leaveallgc</code>
• Penjelasan : Untuk keluar semua dari grup akun anda. 

• Perintah : <code>{0}leaveallch</code>
• Penjelasan : Untuk keluar semua dari channel akun anda.

• Perintah : <code>{0}leave</code> [username]
• Penjelasan : Untuk keluar dari grup dengan username.
"""


@PY.UBOT("kickme|leave", FILTERS.ME_GROUP)
async def _(client, message):
    await leave(client, message)


@PY.UBOT("join")
async def _(client, message):
    await join(client, message)


@PY.UBOT("leaveallgc")
async def _(client, message):
    await kickmeall(client, message)


@PY.UBOT("leaveallch")
async def _(client, message):
    await kickmeallch(client, message)


