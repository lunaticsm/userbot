from ubot import *

__MODULE__ = "Profile"
__HELP__ = """
Bantuan Untuk Profile

• Perintah: <code>{0}adminlist</code>
• Penjelasan: Untuk melihat status admin grup anda.

• Perintah: <code>{0}setbio</code> [query]
• Penjelasan: Untuk mengubah bio Anda.

• Perintah: <code>{0}setname</code> [query]
• Penjelasan: Untuk mengubah Nama Anda.

• Perintah: <code>{0}setpp</code> [balas media]
• Penjelasan: Untuk mengubah Foto Akun Anda.

• Perintah: <code>{0}block</code> [balas pengguna]
• Penjelasan: Untuk blokir pengguna.

• Perintah: <code>{0}unblock</code> [query]
• Penjelasan: Untuk buka blokir pengguna.
"""


@PY.UBOT("setbio")
async def _(client, message):
    await set_bio(client, message)


@PY.UBOT("setname")
async def _(client, message):
    await setname(client, message)


@PY.UBOT("block")
async def _(client, message):
    await block_user_func(client, message)


@PY.UBOT("unblock")
async def _(client, message):
    await unblock_user_func(client, message)


@PY.UBOT("setpp")
async def _(client, message):
    await set_pfp(client, message)

@PY.UBOT("adminlist")
async def _(client, message):
    await list_admin(client, message)