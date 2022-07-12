import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
    
    @commands.command()
    async def hi(self, ctx):
        await ctx.send("ABCC")

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