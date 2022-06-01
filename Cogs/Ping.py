import discord
from discord.ext import commands

import math
class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Latency: {math.ceil(self.client.latency * 1000)} ms")

def setup(client):
    client.add_cog(Ping(client))