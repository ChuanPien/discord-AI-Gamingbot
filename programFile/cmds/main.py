import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

# 打開json並讀取，使用utf8 encode
with open('setting.json', mode='r', encoding='utf8') as jFile:
    jdata = json.load(jFile)


class Main(Cog_Extension):
    @commands.command()
    # 顯示延遲
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)} (ms)')


def setup(bot):
    bot.add_cog(Main(bot))
