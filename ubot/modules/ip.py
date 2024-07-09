from ubot import *


__MODULE__ = "IP Info"
__HELP__ = """
 Bantuan Untuk Info

• Perintah : <code>{0}ipinfo</code> [ip address]
• Penjelasan : Untuk mendapatkan informasi ip address
  """


@PY.UBOT("ipinfo")
async def _(client, message):
    await hacker_lacak_target(client, message)
