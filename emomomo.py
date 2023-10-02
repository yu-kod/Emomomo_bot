import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import demoji

import logging

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
client = discord.Client(intents=intents)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client = commands.Bot(command_prefix='!', intents=intents)

# UNDER THIS LINE OF CODE ARE THE COMMANDS FOR THE BOT. YOU CAN ADD/CHANGE THOSE SAFELY WITHOUT DESTORYING THE CODE

@client.command()
async def emo(ctx):
	await ctx.send("help実装中")


@client.event
async def on_message(message):
    if message.channel.name == "emomomo":
        if message.author.bot:
            return
        text = demoji.replace(message.content, '')
        text = text.strip()
        if text != "":
            await message.delete()

client.run(DISCORD_TOKEN)
