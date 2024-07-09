import asyncio
import random

import requests
from pyrogram import *
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *

from ubot import *


async def salamone(client: Client, message: Message):
    await message.edit(
            "Assalamualaikum Sayang.",
)

async def salamdua(client: Client, message: Message):
    await message.edit(
            "Assalamualaikum Warahmatullahi Wabarakatuh",
    )

async def jwbsalam(client: Client, message: Message):
    await message.edit(
            "Wa'alaikumsalam Kaum Dajjal...",
    )

async def jwbsalamlngkp(client: Client, message: Message):
    await message.edit(
            "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
    )

async def salamarab(client: Client, message: Message):
    xx = await message.edit("Salam Dulu Gua..")
    await asyncio.sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
