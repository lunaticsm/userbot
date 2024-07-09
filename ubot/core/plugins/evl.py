import asyncio
import os
import platform
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO

import psutil

from ubot import *


async def shell_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("noob")
    try:
        if message.command[1] == "restart":
            await message.delete()
            os.execl(sys.executable, sys.executable, "-m", "ubot")
        elif message.command[1] == "gitpull":
            await message.delete()
            os.system(f"kill -9 {os.getpid()} & git pull & python3 -m ubot")
        elif message.command[1] == "clean":
            count = 0
            for X in os.popen("ls").read().split():
                try:
                    os.remove(X)
                    count += 1
                except:
                    pass
            return await message.reply(f"✅ {count} sampah berhasil di bersihkan")
        else:
            msg = await message.reply("<b>Memproses</b>")
            screen = (await bash(message.text.split(None, 1)[1]))[0]
            if int(len(str(screen))) > 4096:
                with BytesIO(str.encode(str(screen))) as out_file:
                    out_file.name = "result.txt"
                    await message.reply_document(
                        document=out_file,
                    )
                    await msg.delete()
            else:
                await message.reply(screen)
                await msg.delete()
    except Exception as error:
        await msg.edit(error)


async def evalator_cmd(client, message):
    if not get_arg(message):
        return
    TM = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]
    reply_to_ = message.reply_to_message or message
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "<b>OUTPUT</b>:\n"
    final_output += f"<b>{evaluation.strip()}</b>"
    if len(final_output) > 4096:
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd[: 4096 // 4 - 1],
                disable_notification=True,
                quote=True,
            )
    else:
        await reply_to_.reply_text(final_output, quote=True)
    await TM.delete()


async def trash_cmd(client, message):
    if message.reply_to_message:
        msg_id = message.reply_to_message.id
    else:
        msg_id = message.id
    try:
        msgs = await client.get_messages(message.chat.id, msg_id)
        if len(str(msgs)) > 4096:
            with BytesIO(str.encode(str(msgs))) as out_file:
                out_file.name = "trash.txt"
                return await message.reply_document(document=out_file)
        else:
            return await message.reply(msgs)
    except Exception as error:
        return await message.reply(str(error))


async def get_my_otp(client, message):
    TM = await message.reply("<b>sᴇᴅᴀɴɢ Processing...</b>", quote=True)
    if len(message.command) < 2:
        return await TM.edit("<b>ᴘᴀʏᴀʜ ɢɪᴛᴜ ᴀᴊᴀ ɴɢɢᴀᴋ ʙɪsᴀ</b>")
    else:
        for X in ubot._ubot:
            if int(message.command[1]) == X.me.id:
                if message.command[0] == "getotp":
                    async for otp in X.search_messages(777000, limit=1):
                        if not otp.text:
                            await message.reply(
                                "<b>❌ ᴋᴏᴅᴇ ᴏᴛᴘ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>", quote=True
                            )
                        else:
                            await message.reply(otp.text, quote=True)
                            await X.delete_messages(X.me.id, otp.id)
                    await TM.delete()
                else:
                    return await TM.edit(X.me.phone_number)


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


async def vps(client, callback_query):
    uname = platform.uname()
    softw = "Informasi Sistem\n"
    softw += f"Sistem   : {uname.system}\n"
    softw += f"Rilis    : {uname.release}\n"
    softw += f"Versi    : {uname.version}\n"
    softw += f"Mesin    : {uname.machine}\n"

    boot_time_timestamp = psutil.boot_time()

    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"Waktu Hidup: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}\n"

    softw += "\nInformasi CPU\n"
    softw += "Physical cores   : " + str(psutil.cpu_count(logical=False)) + "\n"
    softw += "Total cores      : " + str(psutil.cpu_count(logical=True)) + "\n"
    cpufreq = psutil.cpu_freq()
    softw += f"Max Frequency    : {cpufreq.max:.2f}Mhz\n"
    softw += f"Min Frequency    : {cpufreq.min:.2f}Mhz\n"
    softw += f"Current Frequency: {cpufreq.current:.2f}Mhz\n\n"
    softw += "CPU Usage Per Core\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        softw += f"Core {i}  : {percentage}%\n"
    softw += "Total CPU Usage\n"
    softw += f"Semua Core: {psutil.cpu_percent()}%\n"

    softw += "\nBandwith Digunakan\n"
    softw += f"Unggah  : {get_size(psutil.net_io_counters().bytes_sent)}\n"
    softw += f"Download: {get_size(psutil.net_io_counters().bytes_recv)}\n"

    svmem = psutil.virtual_memory()
    softw += "\nMemori Digunakan\n"
    softw += f"Total     : {get_size(svmem.total)}\n"
    softw += f"Available : {get_size(svmem.available)}\n"
    softw += f"Used      : {get_size(svmem.used)}\n"
    softw += f"Percentage: {svmem.percent}%\n"

    msg = await bot.send_message(
        callback_query.from_user.id, f"<b>{Fonts.smallcap(softw.lower())}</b>"
    )
    await asyncio.sleep(15)
    return await msg.delete()


async def cb_restart(client, callback_query):
    await callback_query.message.delete()
    os.system(f"kill -9 {os.getpid()} & python3 -m ubot")


async def cb_gitpull(client, callback_query):
    await callback_query.message.delete()
    os.system(f"kill -9 {os.getpid()} & git pull & python3 -m ubot")
