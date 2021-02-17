
                    ```py
import discord
# importing the general discord package
from discord.ext import commands
# importing the commands extension of discord.py


intents = discord.Intents.default()
intents.members = True
# defining the bots intents

bot = commands.Bot(command_prefx="!", intents=intents)
# creating our bot object

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}\n({bot.user.id})")
    # every time the bot starts, we print its info

bot.run("PASTE YOUR TOKEN HERE")
# running our bot
```
                    