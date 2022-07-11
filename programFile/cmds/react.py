import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    @commands.command()
    async def test(self, ctx, arg):
        await ctx.send(arg)

def setup(bot):
    bot.add_cog(React(bot))