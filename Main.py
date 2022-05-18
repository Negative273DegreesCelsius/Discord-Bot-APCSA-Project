import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

import json

import os

from ... import Helper
from Helper import *

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = ">", intents = intents)

bot_info = get_json("Config.json")

@client.event
async def on_ready():
    # automatically load all cogs on startup
    for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'Cogs.{filename[:-3]}')
    
    print(f"Successfully logged in as {client.user}")

@client.command()
async def load(ctx, extension):
    await client.load_extension(f'Cogs.{extension}')
    await ctx.send(f'{extension} is now loaded')

@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'Cogs.{extension}')
    await ctx.send(f'{extension} is now unloaded')

token = bot_info["token"]
client.run(token)