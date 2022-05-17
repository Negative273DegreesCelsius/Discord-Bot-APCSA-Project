import discord
from discord import commands

class Test:
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def test(self, ctx):
    
def setup(client):
    client.add_cog(Test(client))
