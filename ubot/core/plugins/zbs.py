async def zombies_cmd(client, message):
    chat_id = message.chat.id
    deleted_users = []
    banned_users = 0
    Tm = await message.reply("<code>Processing...</code>")
    async for i in client.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    if len(deleted_users) > 0:
        for deleted_user in deleted_users:
            try:
                banned_users += 1
                await message.chat.ban_member(deleted_user)
            except Exception:
                pass
        await Tm.edit(f"<b>Berhasil mengeluarkan {banned_users} akun terhapus</b>")
    else:
        await Tm.edit("<b>Tidak ada akun terhapus disini.</b>")
