import discord
from discord import commands

class Ping:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Latency: {self.client.latency}")

def setup(client):
    client.add_cog(Ping(client))