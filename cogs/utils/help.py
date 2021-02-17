import discord
from discord.ext import commands

from discord.ext import menus

from cogs.utils.helpers.pagination import ListSource, ReplyMenu, quick_embed_paginate


rose = discord.Colour.from_rgb(250, 218, 221)


class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return f'{self.clean_prefix}{command.qualified_name} {command.signature}'


    async def send_bot_help(self, mapping):
        uembed = discord.Embed(title="Utility Commands", colour = rose)
        uembed.set_footer(text="Page 2/3")
        sembed = discord.Embed(title="Staff Commands", colour = rose)
        sembed.set_footer(text="Page 1/3")
        fembed = discord.Embed(title="Fun Commands", colour = rose)
        fembed.set_footer(text="Page 3/4")
        oembed = discord.Embed(title="Other Commands", colour = rose)
        oembed.set_footer(text="Page 4/4")
        scommands = []
        ucommands = []
        fcommands = []
        ocommands = []
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")

                for command in commands:
                    if command.cog_name == 'latencies' or not command.cog_name:
                        ucommands.append(command)
                    elif command.cog_name == 'StaffCommands' or command.cog_name == 'AntiSwear':
                        scommands.append(command)
                    elif command.cog_name == 'Fun':
                        fcommands.append(command)
                    else:
                        ocommands.append(command)

        for ucommand in ucommands:
            uembed.add_field(name=self.get_command_signature(ucommand), value=f'*{ucommand.help}*', inline=False)
        for scommand in scommands:
            sembed.add_field(name=self.get_command_signature(scommand), value=f'*{scommand.help}*', inline=False)
        for fcommand in fcommands:
            fembed.add_field(name=self.get_command_signature(fcommand), value=f'*{fcommand.help}*', inline=False)
        for ocommand in ocommands:
            oembed.add_field(name=self.get_command_signature(ocommand), value=f'*{ocommand.help}*', inline=False)



        l = ListSource([sembed, uembed, oembed])
        pages = ReplyMenu(source=l)
        await pages.start(ctx=self.context)


    async def send_command_help(self, command):
        embed = discord.Embed(title=f'`{self.get_command_signature(command)}`', description = f'*{command.help}*', colour = rose)
        embed.set_author(name=f'Help for Command: {command.name}')
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)


        await self.context.reply(embed=embed)
