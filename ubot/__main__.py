import asyncio
import os
import sys

from atexit import register
from pyrogram import idle
from pyrogram.errors import RPCError

from ubot import *


async def start_ubot(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=30)
        await ubot_.join_chat("alterbase2")
        await ubot_.join_chat("sexualredroom")
    except asyncio.TimeoutError:
        #await remove_ubot(user_id)
        await add_prem(user_id)
        await sending_user(user_id)
        print(f"✅ {user_id} Gak Respon.")
    except RPCError:
        #await remove_ubot(user_id)
        #await rm_all(user_id)
        #await rem_expired_date(user_id)
        #for X in await get_chat(user_id):
            #await remove_chat(user_id, X)
        print(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")
    except:
        pass


async def main():
    tasks = [
        asyncio.create_task(start_ubot(int(_ubot["name"]), _ubot))
        for _ubot in await get_userbots()
    ]
    await asyncio.gather(*tasks, bot.start())
    await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots(), idle())


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
