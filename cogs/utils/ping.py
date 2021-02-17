import discord
from discord.ext import commands

import time


class latencies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(help="get the bots different pings")
    async def ping(self, ctx):
        start_time = time.time()
        msg = await ctx.send("Testing Ping...")
        end_time = time.time()

        await msg.edit(content=f"BOT: {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")


def setup(bot):
    bot.add_cog(latencies(bot))
