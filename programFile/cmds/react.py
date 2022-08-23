import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    @commands.command()
    async def test(self, ctx, arg):
        await ctx.send(arg)
#測試用指令
    @commands.command()
    async def hi(self, ctx):
        print("HI!~")
        await ctx.send("ABCC")

def setup(bot):
    bot.add_cog(React(bot))