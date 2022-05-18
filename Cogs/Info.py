import discord
from discord.ext import commands

from ... import Helper

from Helper import *

async def get_authors():
    data = get_json("Config.json")
    author_list = data["authors"]
    authors = ""
    for i in range(len(author_list) - 1):
        authors += author_list[i] + ", "
    authors += author_list[len(author_list) - 1]
    return authors

class Info:

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
            value = get_authors(),
            inline = False
        )
        embed.add_field(
            name = "Street view API used: ",
            value = "Mapillary API\nhttps://www.mapillary.com/developer",
            inline = False
        )
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Info(client))