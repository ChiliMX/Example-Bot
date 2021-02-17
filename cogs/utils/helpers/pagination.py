import discord
from discord.ext import menus

class ListSource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=1)

    async def format_page(self, menu, page):
        return page


class ReplyMenu(menus.MenuPages):
    async def send_initial_message(self, ctx, channel):
        page = await self._source.get_page(0)
        kwargs = await self._get_kwargs_from_page(page)
        return await ctx.reply(**kwargs)


def quick_embed_paginate(embeds: list):
    source = ListSource(embeds)
    return ReplyMenu(source=source, clear_reactions_after=True)
