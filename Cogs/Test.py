import discord
from discord.ext import commands

import sys
import random
import asyncio

# get path to import Helper and ShutterstockImg
path = sys.path[0]
path = path[:path.rfind("\\")]

sys.path.insert(1, path)

from ShutterstockImg import ShutterstockImg
from Helper import *
class Test(commands.Cog):
    def __init__(self, client):
        self.client = client
  
    @commands.command()
    async def test(self, ctx):
        guesses = 3

        country_data = get_json("Data.json")
        country = random.choice(list(country_data))
        capital = country_data[str(country)]["capital"][0]
        search_query = f"{capital}, {country} buildings"

        answer = f"{capital.upper()}, {country.upper()}"

        ImgObj = ShutterstockImg(search_query, 5)
        img_url_list = ImgObj.get_url_list()
        embed_list = []
        page = 0
        for url in img_url_list:
            em = discord.Embed(
                title = "Guess the country/capital",
                description = f"Enter the name of the country or capital ONLY",
                color = discord.Colour.blue()
            )
            em.set_image(url = url)
            embed_list.append(em)

        msg = await ctx.send(embed = embed_list[page])
        await msg.add_reaction("◀️")
        await msg.add_reaction("▶️")

        def check_reaction(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        
        def check_user(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        
        while True:
            try:
                '''
                The following code snippet with handling pending tasks
                was inspired by Achxy_'s answer on StackOverflow
                https://stackoverflow.com/a/70661168
                '''
                pending_tasks = [
                    self.client.loop.create_task(self.client.wait_for('message', check = check_user)),
                    self.client.loop.create_task(self.client.wait_for('reaction_add', check = check_reaction))
                ]
                done, pending = await asyncio.wait(pending_tasks, return_when=asyncio.FIRST_COMPLETED)
                task = done.pop()

                try:
                    reaction, user = await task
                    if str(reaction.emoji) == "▶️" and page != int(len(img_url_list) - 1):
                        page += 1
                        await msg.edit(embed = embed_list[page])
                        await msg.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "◀️" and page > 0:
                        page -= 1
                        await msg.edit(embed = embed_list[page])
                        await msg.remove_reaction(reaction, user)
                    else:
                        await msg.remove_reaction(reaction, user)
                except TypeError:
                    response = ((await task).content).lower()
                    if (response in country_data[country]["capital"]) or (response == country.lower() or (response in country_data[country]["alternative_names"])):
                        await ctx.reply("Correct!")
                        break
                    else:
                        guesses -= 1
                        if guesses == 0:
                            await ctx.reply(f"You ran out of guesses. The answer was {answer}")
                            break
                        else:
                            await ctx.reply(f"Incorrect. You have {guesses} guesses remaining")
            except asyncio.TimeoutError:
                await ctx.reply(f"You ran out of time. The answer was {answer}")
                break

    
def setup(client):
    client.add_cog(Test(client))
