from ubot import *

__MODULE__ = "Gcast"
__HELP__ = """
 Bantuan Untuk Gcast

• Perintah : <code>{0}ucast</code> [balas pesan/kirim pesan]
• Penjelasan : Untuk pengirim pesan ke semua pengguna.

• Perintah : <code>{0}gcast</code> [balas pesan/kirim pesan]
• Penjelasan : Untuk pengirim pesan ke semua grup.

• Perintah : <code>{0}sgcast</code>
• Penjelasan : Untuk membatalkan proses gcast.

• Perintah : <code>{0}send</code> [username/user_id - teks/reply]
• Penjelasan : Untuk mengirim pesan ke pengguna/grup/channel.
  
• Untuk Menggunakan Button Gunakan Format : <code> Teks ~ button_teks:button_url</code>
"""


@PY.UBOT("gcast")
async def _(client, message):
    await broadcast_group_cmd(client, message)


@PY.UBOT("ucast")
async def _(client, message):
    await broadcast_users_cmd(client, message)


@PY.UBOT("sgcast")
async def _(client, message):
    await cancel_broadcast(client, message)

@PY.UBOT("send")
async def _(client, message):
    await send_msg_cmd(client, message)


@PY.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)


@PY.INLINE("^gcast_button")
@INLINE.QUERY
async def _(client, inline_query):
    await gcast_inline(client, inline_query)
