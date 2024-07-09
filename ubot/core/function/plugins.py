from importlib import import_module
from platform import python_version

from pyrogram import __version__
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ubot import bot, ubot
from ubot.config import OWNER_ID
from ubot.core.helpers import PY
from ubot.modules import loadModule

HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = import_module(f"ubot.modules.{mod}")
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELP_COMMANDS[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module
    print(f"[🤖 @{bot.me.username} 🤖] [🔥 TELAH BERHASIL DIAKTIFKAN! 🔥]")
    await bot.send_message(OWNER_ID, f"""
<b>🤖 {bot.me.mention} Aktif</b>

<b>Modules : {len(HELP_COMMANDS)}</b>
<b>Python : {python_version()}</b>
<b>Pyrogram : {__version__}</b>
<b>Users : {len(ubot._ubot)}</b>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Git Pull", callback_data="gitpull"),
                    InlineKeyboardButton("Restart", callback_data="restart"),
                ],
            ]
        ),
    )

async def loadPlugins2():
    modules = loadModule()
    for mod in modules:
        imported_module = import_module(f"ubot.modules.{mod}")
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELP_COMMANDS[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module

@PY.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
