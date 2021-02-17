import discord
from discord.ext import commands

from datetime import datetime
import asyncio


class StaffCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="kicks the mentioned user from the guild")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.member, *, reason="breaking the rules"):
        embed = discord.Embed(
            colour=discord.Colour.default(),
            timestamp=datetime.now()
        )

        embed.add_field(name=f"kicked {member}", value=f"{member} was kicked by {ctx.author} for: {reason}")
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

        await ctx.guild.kick(member, reason=reason)

    @commands.command(help="bans the mentioned user from the guild")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="banned for breaking the rules"):
        embed = discord.Embed(
            colour=discord.Colour.default(),
            timestamp=datetime.now()
        )

        embed.add_field(name=f"banned {member}", value=f"{member} was banned by {ctx.author} for: {reason}")

        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

        await ctx.guild.ban(member, reason=reason)

    @commands.command(help="unbans the user mentioned via ID")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        member = discord.Object(id=id)

        embed = discord.Embed(
            colour=discord.Colour.default(),
            timestamp=datetime.now()
        )

        embed.add_field(name=f"unbanned {member}", value=f"{member} was unbanned by {ctx.author}")
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

        await ctx.guild.unban(member)

    @commands.command(aliases=['clear', 'delete', 'del'], help="purges a set amount of messages")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.send(f"now purging {amount} messages", delete_after=2)

        await asyncio.sleep(2.0)

        await ctx.message.delete()

        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(StaffCommands(bot))
