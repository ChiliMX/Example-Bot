import discord
from discord.ext import commands
# discord imports

import json
from datetime import datetime

def privatechannel():
    def predicate(ctx):

        return (
                not ctx.channel.overwrites_for(ctx.guild.default_role).view_channel
                and ctx.channel.overwrites_for(ctx.guild.default_role).view_channel is not None
        )

    return commands.check(predicate)


class AntiSwear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            with open('cogs/staff/filters/words.json') as f:
                data = json.load(f)

                for w in data:
                    if w in message.content.lower():
                        embed = discord.Embed(
                            colour = discord.Colour.default(),
                            timestamp=datetime.now()
                        )

                        embed.add_field(name="Deleted Message", value=f"Deleted message from {message.author}")
                        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)

                        await message.delete()
                        await message.channel.send(embed=embed)

    @commands.command(aliases=["addword", "nswear"], help="adds the specified word to the banned word list")
    @commands.has_permissions(administrator=True)
    @privatechannel()
    async def swappend(self, ctx, *, content):

        with open('cogs/staff/filters/words.json') as f:
            words = json.load(f)

        words.append(content)

        with open('cogs/staff/filters/words.json') as f:
            json.dump(words, f)

            embed = discord.Embed(
                colour=discord.Colour.default(),
                timestamp=datetime.now()
            )

            embed.add_field(name="Added word to the blacklisted words", value=f"{ctx.author} has added the word ||{content}|| into the blacklisted word list")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

            await ctx.message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(AntiSwear(bot))
