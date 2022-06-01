import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

import sys, os

path = sys.path[0]
path = path[:path.rfind("\\")]

from Helper import *

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = ">", intents = intents)

bot_info = get_json("Config.json")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        em = discord.Embed(
            title = "Error!",
            description = "An error has been found.",
            color = discord.Colour.red()
        )
        em.add_field(
            name = "Command not found",
            value = "The command you used does not exist. Please use apush.help to see a list of commands",
            inline = False
        )
        await ctx.reply(embed = em)
        return
    raise error

@client.event
async def on_ready():
    # automatically load all cogs on startup
    for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'Cogs.{filename[:-3]}')
    
    print(f"Successfully logged in as {client.user}")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')
    await ctx.send(f'{extension} is now loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    await ctx.send(f'{extension} is now unloaded')

token = bot_info["token"]
client.run(token)