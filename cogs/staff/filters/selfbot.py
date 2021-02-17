import discord
from discord.ext import commands

from datetime import datetime


class SelfBotFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            if message.embeds and message.content.count("https://") < len(message.embeds):
                embed = discord.Embed(
                    colour=discord.Colour.default(),
                    timestamp=datetime.now()
                )

                embed.add_field(name="SelfBot detected", value=f"{message.author} has set off the SelfBot filter")
                embed.set_footer(text=message.author, icon_url=message.author.avatar_url)

                await message.guild.owner.send(embed=embed)


def setup(bot):
    bot.add_cog(SelfBotFilter(bot))
