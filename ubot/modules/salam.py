from ubot import *

__MODULE__ = "Salam"
__HELP__ = """
Bantuan Untuk Salam


• Perintah: <code>{0}p</code>
• Penjelasan: Coba aja sendiri.

• Perintah: <code>{0}pe</code>
• Penjelasan: Coba aja sendiri.

• Perintah: <code>{0}l</code>
• Penjelasan: Coba aja sendiri.

• Perintah: <code>{0}el</code>
• Penjelasan: Coba aja sendiri.

• Perintah: <code>{0}as</code>
• Penjelasan: Coba aja sendiri.

"""


@PY.UBOT("p")
async def _(client, message):
    await salamone(client, message)


@PY.UBOT("pe")
async def _(client, message):
    await salamdua(client, message)


@PY.UBOT("l")
async def _(client, message):
    await jwbsalam(client, message)


@PY.UBOT("el")
async def _(client, message):
    await jwbsalamlngkp(client, message)


@PY.UBOT("as")
async def _(client, message):
    await salamarab(client, message)
