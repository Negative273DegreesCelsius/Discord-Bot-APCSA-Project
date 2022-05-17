import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

import json

import os

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
    # automatically load all cogs on startup
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
    
    print(f"Successfully logged in as {client.user}")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} is now loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} is now unloaded')
