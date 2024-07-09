from ubot import *


__MODULE__ = "ShowID"
__HELP__ = """
Bantuan Untuk Show ID

• Perintah: <code>{0}id</code>
• Penjelasan: Untuk mengetahui ID dari user/grup/channel.

• Perintah: <code>{0}id</code> [reply to user/media]
• Penjelasan: Untuk mengetahui ID dari user/media.

• Perintah: <code>{0}getid</code> [username user/grup/channel].
• Penjelasan: Untuk mengetahui ID user/grup/channel melalui username dengan simbol @.
"""


@PY.UBOT("id")
async def _(client, message):
    await id_cmd(client, message)
