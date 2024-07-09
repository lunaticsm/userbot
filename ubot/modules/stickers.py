from ubot import *

__MODULE__ = "Stickers"
__HELP__ = """
Bantuan Untuk Stickers

• Perintah: <code>{0}q</code> [text/reply to text/media]
• Penjelasan: Untuk merubah text menjadi sticker.

• Perintah: <code>{0}qf</code> [@username text]
• Penjelasan: Make fake quote.

• Perintah: <code>{0}q</code> [white/black/red/pink]
• Penjelasan: Untuk merubah latar belakang quote.

• Perintah : <code>{0}kang</code> [balas ke stiker]
• Penjelasan : Untuk membuat kostum stiker pack.
"""


@PY.UBOT("q")
async def _(client, message):
    await quotly_cmd(client, message)

@PY.UBOT("qf")
async def _(client, message):
    await fake_quote_cmd(client, message)

#@PY.BOT("kang")
#async def _(client, message):
    #await kang_cmd_bot(client, message)


@PY.UBOT("kang")
async def _(client, message):
    await kang(client, message)
