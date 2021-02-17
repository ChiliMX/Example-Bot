import discord
from discord.ext import commands

import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball", help="an 8ball command that acts like an 8ball and responds to the inputed question")
    async def _8ball(self, ctx, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so goodt.",
                     "Very doubtful."]

        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(help="pays respects")
    async def f(self, ctx):
        await ctx.send("F in chat")
