import discord
from discord.ext import commands

import time

# creating our new cog
class latencies(commands.Cog):

    """
    initializing the class
    defining bot
    """

    def __init__(self, bot):
        self.bot = bot


    @commands.command(help="get the bots different pings")
    async def ping(self, ctx):
        # starting our ping counter
        start_time = time.time()
        msg = await ctx.send("Testing Ping...")
        # ending our ping counter
        end_time = time.time()

        """
        editing our original message to display the bots different pings
        """

        await msg.edit(content=f"BOT: {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")



def setup(bot):
    # setting up our cog
    bot.add_cog(latencies(bot))
