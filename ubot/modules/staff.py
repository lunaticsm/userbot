from ubot import *

__MODULE__ = "Staff"
__HELP__ = """
Bantuan Untuk Staff

• Perintah: <code>{0}staff</code>
• Penjelasan: Untuk mengetahui daftar semua admin didalam grup.
"""

@PY.UBOT("staff")
async def _(client, message):
    await staff_cmd(client, message)
