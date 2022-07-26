import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

#打開json並讀取，使用utf8 encode
with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

class Main(Cog_Extension):
    @commands.command()
#顯示延遲
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

#機器人幫你發話，並刪除指令發送訊息
#*,msg *後面任何arge都會被讀取
    @commands.command()
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send (msg)

#del 訊息
    @commands.command()
    async def clean (self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)



def setup(bot):
    bot.add_cog(Main(bot))