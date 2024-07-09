


from datetime import datetime, timedelta
from pyrogram import Client, filters
from pytimeparse import parse
from pytz import timezone

from ubot import *

# Daftar pengingat yang tersimpan

reminders = []



async def reminder(client, message):
    prefix = await get_prefix(client.me.id)
    if len(message.command) == 1 or len(message.command) == 2:
        await message.reply(f"Penggunaan: `remind <waktu> <pesan>`\n\nContoh:\n`{next((p) for p in prefix)}remind 1j30m Beli susu`\n`{next((p) for p in prefix)}remind 1h30m Cek email`")
    else:
        time_from_now = message.command[1]
        text_to_remind = message.text.split(" ", 2)[2]
        now = datetime.now(timezone("Asia/Jakarta"))
        delay = parse(time_from_now)
        t = now + timedelta(seconds=delay)

        reminders.append((t, text_to_remind))
        await client.send_message(message.chat.id, text_to_remind, schedule_date=t)
        await message.reply(f"Pengingat disimpan, akan dikirim pada {t.strftime('%d/%m/%Y')} pukul {t.strftime('%H:%M:%S')}.")



async def listrem(client, message):
    if len(reminders) == 0:
        await message.reply("Tidak ada pengingat yang tersimpan.")
    else:
        response = "Daftar Pengingat:\n\n"
        for i, reminder in enumerate(reminders, start=1):
            t, text = reminder
            response += f"{i}. {text} - {t.strftime('%d/%m/%Y %H:%M:%S')}\n"
        await message.reply(response)
