import discord
from discord.ext import commands

import os
from constants import PREFIX

from cogs.utils.help import MyHelp

from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True

allowed_mentions = discord.AllowedMentions(roles=True,
                                           users=True,
                                           everyone=False)

bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX),
                   intents=intents, allowed_mentions=allowed_mentions,
                   activity=discord.Game(name="Setting a Good Example"),
                   help_command=MyHelp())


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}\n({bot.user.id})")


extensions = ['cogs.staff.moderation',
              'cogs.utils.ping',
              'cogs.staff.filters.antiswear',
              'cogs.staff.filters.selfbot',
              'cogs.tags.tag',
              'cogs.utils.errors',
              'cogs.staff.modmail.modmail'
              ]

for extension in extensions:
    bot.load_extension(extension)


load_dotenv()

bot.run(os.getenv("TOKEN"))

