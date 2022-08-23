from bitarray import test
import discord
from discord.ext import commands
import scipy as sp
from core.classes import Cog_Extension,Global_Data
from WEB_REQUESTS.testPOEweb import testPOE

class React(Cog_Extension):
    @commands.command()
    async def test(self, ctx, arg):
        await ctx.send(arg)
#測試用指令
    @commands.command()
    async def hi(self, ctx):
        print("HI!~")
        await ctx.send("ABCC")
    #testPOE
    @commands.command()
    async def poe(self, ctx, *,msg):
        #分割訊息
        sp_msg = msg
        sp_msg = sp_msg.split(" ")
        #初始化查詢模塊
        tpoe = testPOE(sp_msg[0],sp_msg[1])
        tpoe.chromedriver()
        report_msg = Global_Data.search_reactMsg
        await ctx.send(report_msg)
    

def setup(bot):
    bot.add_cog(React(bot))