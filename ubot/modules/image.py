from ubot import *

__MODULE__ = "Image"
__HELP__ = """
 Bantuan Untuk Image

• Perintah : <code>{0}rbg</code> [balas foto]
• Penjelasan : Untuk menghapus latar belakang gambar.

• Perintah : <code>{0}blur</code> [balas foto]
• Penjelasan : Untuk memberikan efek blur ke gambar.

• Perintah : <code>{0}miror</code> [balas foto]
• Penjelasan : Untuk memberikan efek cermin ke gambar.

• Perintah : <code>{0}negative</code> [balas foto]
• Penjelasan : Untuk memberikan efek negative ke gambar.
"""


@PY.UBOT("rbg")
async def _(client, message):
    await rbg_cmd(client, message)


@PY.UBOT("blur")
async def _(client, message):
    await blur_cmd(client, message)


@PY.UBOT("negative")
async def _(client, message):
    await negative_cmd(client, message)


@PY.UBOT("miror")
async def _(client, message):
    await miror_cmd(client, message)
