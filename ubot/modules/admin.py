from ubot import *

__MODULE__ = "Admin"
__HELP__ = """
 Bantuan Untuk Admin

• Perintah : <code>{0}kick or dkick</code> [user_id/username/reply user]
• Penjelasan : Untuk menendang anggota dari grup.

• Perintah : <code>{0}ban or dban </code> [user_id/username/reply user]
• Penjelasan : Untuk memblokir anggota dari grup.

• Perintah : <code>{0}mute</code> [user_id/username/reply user]
• Penjelasan : Untuk membisukan anggota dari grup.

• Perintah : <code>{0}unban</code> [user_id/username/reply user]
• Penjelasan : Untuk melepas pemblokiran anggota dari grup.

• Perintah : <code>{0}unmute</code> [user_id/username/reply user]
• Penjelasan : Untuk melepas pembisuan anggota dari grup.
"""


@PY.UBOT("kick|ban|mute|unmute|unban", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_bannen(client, message)

@PY.UBOT("pin|unpin", FILTERS.ME_GROUP)
async def _(client, message):
    await pin_message(client, message)

@PY.UBOT("promote|fullpromote", FILTERS.ME_GROUP)
async def _(client, message):
    await promotte(client, message)

@PY.UBOT("demote", FILTERS.ME_GROUP)
async def _(client, message):
    await demote(client, message)