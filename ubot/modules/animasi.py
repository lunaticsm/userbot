from ubot import *

__MODULE__ = "Animasi"
__HELP__ = """
 Bantuan Untuk Animasi

• Perintah: <code>{0}loveyou or {0}hmm</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}kntl</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}penis</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}heli or {0}tembak</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}bundir or {0}awk</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}y or {0}tank</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}ajg or {0}babi</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}nah or {0}spongebob</code>
• Penjelasan: Coba sendiri.

• Perintah:  <code>{0}ange or {0}lipkol</code>
• Penjelasan:  Coba sendiri.

• Perintah:  <code>{0}nakal or {0}piss</code>
• Penjelasan:  Coba sendiri.

• Perintah:  <code>{0}kocok</code>
• Penjelasan:  Coba sendiri.
"""


@PY.UBOT("loveyou")
async def _(client, message):
    await lopeyo(client, message)

@PY.UBOT("hmm")
async def _(client, message):
    await hmmm(client, message)


@PY.UBOT("nah")
async def _(client, message):
    await nahlove(client, message)


@PY.UBOT("kntl|kontol")
async def _(client, message):
    await kntl(client, message)

@PY.UBOT("penis|titid")
async def _(client, message):
    await pns(client, message)

@PY.UBOT("heli")
async def _(client, message):
    await helikopter(client, message)

@PY.UBOT("tembak")
async def _(client, message):
    await dornembak(client, message)

@PY.UBOT("bundir")
async def _(client, message):
    await ngebundir(client, message)

@PY.UBOT("awk")
async def _(client, message):
    await awikwok(client, message)

@PY.UBOT("y")
async def _(client, message):
    await ysaja(client, message)

@PY.UBOT("tank")
async def _(client, message):
    await tank(client, message)

@PY.UBOT("babi")
async def _(client, message):
    await babi(client, message)

@PY.UBOT("ajg")
async def _(client, message):
    await anjg(client, message)

@PY.UBOT("ange")
async def _(client, message):
    await piciieess(client, message)

@PY.UBOT("lipkol")
async def _(client, message):
    await lipkoll(client, message)

@PY.UBOT("nakal")
async def _(client, message):
    await nakall(client, message)

@PY.UBOT("piss")
async def _(client, message):
    await peace(client, message)


@PY.UBOT("spongebob")
async def _(client, message):
    await spongebobss(client, message)

@PY.UBOT("kocok")
async def _(client, message):
    await kocokk(client, message)
