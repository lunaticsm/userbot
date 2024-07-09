from ubot import *

__MODULE__ = "Invite"
__HELP__ = """
 Bantuan Untuk Invite

• Perintah : <code>{0}invite</code> [username] 
• Penjelasan : Untuk mengundang anggota ke grup.

• Perintah : <code>{0}inviteall</code> [username grup - cooldwon - anggota]
• Penjelasan : Untuk mengundang anggota ke grup anda. 

• Perintah : <code>{0}cancel</code>
• Penjelasan : Untuk membatalkan proses invite.
  """


@PY.UBOT("invite")
async def _(client, message):
    await invite_cmd(client, message)


@PY.UBOT("inviteall")
async def _(client, message):
    await inviteall_cmd(client, message)


@PY.UBOT("cancel")
async def _(client, message):
    await cancel_cmd(client, message)
