

from ubot import *


__MODULE__ = "Locks"
__HELP__ = """
 Bantuan Untuk Locks

• Perintah : `{0}lock [all or type]`
• Penjelasan : Untuk mengubah izin grup.

• Perintah : `{0}unlock [all or type]`
• Penjelasan : Untuk membuka izin grup.

• Perintah : `{0}locks`
• Penjelasan : Untuk melihat izin saat ini.

• Type : `msg`|`media`|`stickers`|`polls`|`info`|`invite`|`webprev`|`pin`
"""


@PY.UBOT("lock|unlock")
async def _(client, message):
    await locks_func(client, message)


@PY.UBOT("locks")
async def _(client, message):
    await locktypes(client, message)