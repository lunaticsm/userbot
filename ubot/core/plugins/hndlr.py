import asyncio

from ubot import *


async def kok_anjeng(client, message):
    Tm = await message.edit("`Processing...`")
    if len(message.command) < 2:
        return await Tm.edit(f"Prefix harus berupa trigger.")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(client.me.id, ub_prefix)
            await set_pref(client.me.id, ub_prefix)
            parsed_prefix = " ".join(f"{prefix}" for prefix in ub_prefix)
            return await Tm.edit(
                f"✅ Prefix diatur ke : {parsed_prefix}"
            )
        except Exception as error:
            await Tm.edit(str(error))