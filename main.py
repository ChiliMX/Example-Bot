import discord
from discord.ext import commands

import os

# importing our prefix
from constants import PREFIX

# importing our new help command
from cogs.utils.help import MyHelp

# used for accessing our bot token
from dotenv import load_dotenv

# defining the bots intents
intents = discord.Intents.default()
intents.members = True


"""
allowed_mentions is the type of objects our bot can mention.
Here we are make our bot only able to ping @roles and @users, not @everyone or @here
"""

allowed_mentions = discord.AllowedMentions(roles=True,
                                           users=True,
                                           everyone=False)

"""
Here we are creating our bot object and setting our
1) prefix
2) intents
3) allowed_mentions
4) status
5) help command
"""

bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX),
                   intents=intents, allowed_mentions=allowed_mentions,
                   activity=discord.Game(name="Setting a Good Example"),
                   help_command=MyHelp())


@bot.event
async def on_ready():
    # print bot info whenever it starts
    print(f"Logged in as {bot.user}\n({bot.user.id})")


# all our extensions
extensions = ['cogs.staff.moderation',
              'cogs.utils.ping',
              'cogs.staff.filters.antiswear',
              'cogs.staff.filters.selfbot',
              'cogs.tags.tag',
              'cogs.utils.errors',
              'cogs.staff.modmail.modmail'
              ]

# loading the extensions
for extension in extensions:
    bot.load_extension(extension)

# load environment variables(bot token)
load_dotenv()

# running the bot
bot.run(os.getenv("TOKEN"))
