from ubot import *



async def cb_tutor(client, callback_query):
    await callback_query.edit_message_text(
        text="""<b>Tutorial Membuat Userbot :</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Admin", callback_data="start_admin"),
                ],
                [
                    InlineKeyboardButton(text="Tutorial Ambil API ID", url="https://t.me/loghimikoubot/6"),
                    InlineKeyboardButton(text="Tutorial Buat Userbot", url="https://t.me/loghimikoubot/7"),
                ],
                [
                    InlineKeyboardButton(text="Kembali", callback_data="start0"),
                ],
            ]
        ),
    )
    

async def asdksd(client, callback_query):
    if callback_query.from_user.id in DEVS:
        buttons = [
            [InlineKeyboardButton("Buat Userbot", callback_data="bahan"),
            InlineKeyboardButton("Tutorial", callback_data="cb_tutor"),
            ],
            [
                InlineKeyboardButton("Menu Bantuan", callback_data="help_back"),
                InlineKeyboardButton("Pertanyaan", callback_data="support"),
            ],
            [
                InlineKeyboardButton("Status Akun", callback_data="start_profile")],
          ]
    else:
        buttons = [
            [InlineKeyboardButton("Buat Userbot", callback_data="bahan"),
            InlineKeyboardButton("Tutorial", callback_data="cb_tutor"),
            ],
            [
                InlineKeyboardButton("Menu Bantuan", callback_data="help_back"),
                InlineKeyboardButton("Pertanyaan", callback_data="support"),
            ],
            [
                InlineKeyboardButton("Status Akun", callback_data="start_profile")],
          ]
    msg = f"""
<b>👋 Halo {callback_query.from_user.first_name} !!

Apa Ada Yang Bisa Saya Bantu ? Jika Kamu Sudah Melakukan Pembayaran Silakan Klik Tombol Buat Userbot.

Atau Kamu Bisa Melihat Tutorial Terlebih Dahulu Untuk Membuat Userbot.

Dan Jika Kamu Belum Mendapatkan Akses Silakan Contact Admin Untuk Meminta Akses, Serta Kirimkan Bukti Tangkapan Layar Pembayaran.</b>
"""
    await callback_query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(buttons))
    await add_served_user(callback_query.from_user.id)


