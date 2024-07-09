from ubot import *

__MODULE__ = "Limit"
__HELP__ = """
 Bantuan Untuk Limit

• Perintah : <code>{0}limit</code>
• Penjelasan : Untuk mengecek akun anda terbatas atau tidak.
"""


@PY.UBOT("limit")
async def _(client, message):
    await limit_cmd(client, message)
