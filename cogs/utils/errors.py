import discord
from discord.ext import commands


from datetime import datetime


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        error = getattr(error, 'original', error)

        ignored = (commands.CommandNotFound, commands.CheckFailure)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"Bad Argument in {ctx.command}")
            await ctx.send_help(ctx.command)

        elif isinstance(error, discord.HTTPException):
            await ctx.send("an HTTP exception occurred, please try again later.")

        elif isinstance(error, commands.TooManyArguments):
            await ctx.send(f"sorry {ctx.author.mention}, you entered too many arguments. Please try again with the correct amount of arguments.")
            await ctx.send_help(ctx.command)

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention}, you are missing at least one required argument. See below")
            await ctx.send_help(ctx.command)

        else:
            embed = discord.Embed(
                colour = discord.Colour.default(),
                timestamp = datetime.now()
            )
            embed.add_field(name=f'Ignoring exception in command {ctx.command}', value=f"{type(error)}: {error}")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
