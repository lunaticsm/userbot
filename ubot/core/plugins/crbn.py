from ubot import *
from io import BytesIO


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    ex = await message.reply("Processing...")
    carbon = await make_carbon(text)
    await ex.edit("Uploading...")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"<b>Carbonised By : </b>{client.me.mention}",
        ),
    )
    carbon.close()
