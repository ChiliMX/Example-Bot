import discord
from discord.ext import commands
from discord.ext import menus

import json
import os

from cogs.utils.helpers.pagination import ListSource, ReplyMenu, quick_embed_paginate

from constants import PREFIX

rose = discord.Colour.from_rgb(250, 218, 221)


def tags():
    with open('cogs/tags/ltags.json') as f:
        data = json.load(f)
        return list(data)


class Tag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def fetch_close_tags(self, ctx, tag):
        ctags = []
        for name in tags():
            if tag in name:
                ctags.append(name)
        embed = discord.Embed(title='unable to find tag', colour=rose)
        embed.add_field(name="did you mean", value='\n'.join(ctag for ctag in ctags), inline=False)

        return await ctx.reply(embed=embed)

    @commands.command(help="sends a paginated embed with all tags")
    async def tags(self, ctx):
        embed1 = discord.Embed(colour = rose)
        embed1.add_field(name="Tags:", value='\n'.join(key for key in tags()), inline=False)
        embed1.set_footer(text="Page 1/1")

        l = ListSource([embed1])
        pages = ReplyMenu(source=l)
        await pages.start(ctx=ctx)


    @commands.group(help="helpful tags for specific things", aliases=['t'], invoke_without_command=True)
    async def tag(self, ctx):
        return


    @tag.command(help="creates a new tag", aliases=['a', 'c', 'create'])
    async def add(self, ctx, *, name):

        await ctx.send("what would you like the tag to say?")

        tagc = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)

        tagc = tagc.content

        name = name.lower()

        with open('cogs/tags/ltags.json') as f:
            data = json.load(f)

        try:
            if not data[name]:
                data.update({name:f'cogs.utils.tags.{name}.md'})
        except:
            data.update({name: f'cogs/tags/tagfiles/{name}.md'})

            with open('cogs/tags/ltags.json', 'w') as f:
                json.dump(data, f)

            with open(f'cogs/tags/tagfiles/{name}.md', 'w') as newt:
                newt.write(f"""
                {tagc}
                """)

                await ctx.send(f"Created tag {name} with the follwoing content: {tagc}")
        else:
            await ctx.send(f'Sorry {ctx.author.mention}, the tag "{name}" already exists. Try {PREFIX}{name}')



    @tag.command(help="searches for the specified tag", aliases=['s', 'f', 'find'])
    async def search(self, ctx, *, tagn):
        with open('cogs/tags/ltags.json') as f:
            data = json.load(f)

            tag = tagn.lower()

            try:
                if data[tag]:
                    tagcjoin = []

                    with open(data[tag]) as tagc:
                        for w in tagc:
                            tagcjoin.append(w)

                        embed = discord.Embed(title=tagn.upper(), description=''.join(l for l in tagcjoin))

                        await ctx.reply(embed=embed)

            except:
                await self.fetch_close_tags(ctx, tag)

    @tag.command(help="edits the content of the specified tag", aliases=['e', 'change'])
    async def edit(self, ctx, *, tag):
        tag = tag.lower()

        await ctx.send("what would you like the tags new content to be?")
        ntagc = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)

        ntagc = ntagc.content

        with open('cogs/tags/ltags.json') as f:
            data = json.load(f)

            try:
                with open(data[tag], 'w') as ctag:
                    ctag.truncate(0)

                    ctag.write(f"""
                    {ntagc}
                    """)

                await ctx.send(f'set content for tag "{tag} as {ntagc}"')
            except:
                await self.fetch_close_tags(ctx, tag)

    @tag.command(help="removes the specified tag", aliases=['r', 'd', 'del', 'delete'])
    async def remove(self, ctx, *, tagn):
        tagn = tagn.lower()

        with open('cogs/tags/ltags.json') as f:
            data = json.load(f)

            try:
                if data[tagn]:
                    with open('cogs/tags/ltags.json', 'r') as f:
                        data = json.load(f)

                        os.remove(data[tagn])

                        del data[tagn]

                    with open('cogs/tags/ltags.json', 'w') as f:
                        json.dump(data, f)

                    await ctx.reply(f'successfully deleted tag "{tagn}')
            except:
                await self.fetch_close_tags(ctx, tagn)


def setup(bot):
    bot.add_cog(Tag(bot))
