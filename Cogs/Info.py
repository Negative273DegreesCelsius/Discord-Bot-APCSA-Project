import discord
from discord.ext import commands

import sys

# get path to import Helper.py
path = sys.path[0]
path = path[:path.rfind("\\")]

sys.path.insert(1, path)

from Helper import *

async def get_authors():
    data = get_json("Config.json")
    author_list = data["authors"]
    authors = ""
    for i in range(len(author_list) - 1):
        authors += author_list[i] + ", "
    authors += author_list[len(author_list) - 1]
    return authors

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            title = "Bot Info:",
            color = discord.Colour.green()
        )
        embed.add_field(
            name = "Programmed by these users:",
            value = await get_authors(),
            inline = False
        )
        embed.add_field(
            name = "Inspired by Geoguessr",
            value = "https://www.geoguessr.com/",
            inline = False
        )
        embed.add_field(
            name = "Image API used: ",
            value = "Shutterstock API\nhttps://www.shutterstock.com/developers",
            inline = False
        )
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Info(client))
