from ubot import *

__MODULE__ = "Notes"
__HELP__ = """
 Bantuan Untuk Notes

• Perintah : <code>{0}addnote</code> [nama - balas pesan]
• Penjelasan : Untuk menyimpan catatan.

• Perintah : <code>{0}get</code> [nama]
• Penjelasan : Untuk mengambil catatan yang tersimpan.

• Perintah : <code>{0}delnote</code> [ɴᴏᴛᴇ_ɴᴀᴍᴇ]
• Penjelasan : Untuk menghapus nama catatan.

• Perintah : <code>{0}notes</code>
• Penjelasan : Untuk melihat daftar catatan yang disimpan.

• Untuk menggunakan button, Gunakan format :</b>
  <code>teks ~ button teks|button link</code>
"""


@PY.UBOT("addnote")
async def _(client, message):
    await addnote_cmd(client, message)


@PY.UBOT("get")
async def _(client, message):
    await get_cmd(client, message)


@PY.INLINE("^get_notes")
@INLINE.QUERY
async def _(client, inline_query):
    await get_notes_button(client, inline_query)


@PY.UBOT("delnote")
async def _(client, message):
    await delnote_cmd(client, message)


@PY.UBOT("notes")
async def _(client, message):
    await notes_cmd(client, message)
