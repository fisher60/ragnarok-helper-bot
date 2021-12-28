import aiohttp
import logging

import disnake
from disnake.ext import commands


from .settings import API_BASE_URL, BOT_TOKEN, COMMAND_PREFIX, DEBUG, STATIC_DIR, TEST_GUILD_IDS

logging.basicConfig(level=logging.INFO)

if DEBUG:
    bot = commands.Bot(command_prefix=COMMAND_PREFIX, test_guilds=TEST_GUILD_IDS, sync_commands_debug=True)
else:
    bot = commands.Bot(command_prefix=COMMAND_PREFIX)

def format_path(lab_path: list) -> str:
    str_list = [str(x) for x in lab_path]
    return "->".join(str_list)

@bot.slash_command()
async def labyrinth_path(inter, start_location: int, end_location: int):
    async with aiohttp.ClientSession() as session:
        resp = await (await session.get(f"{API_BASE_URL}/find_labyrinth_path", params={"start_location": start_location, "end_location": end_location})).json()
    await inter.response.send_message(format_path(resp.get("path")))

@bot.slash_command()
async def map(inter):
    image_file = disnake.File(f"{STATIC_DIR}/map.png", filename="map.png")
    await inter.response.send_message(file=image_file)

bot.run(BOT_TOKEN)
