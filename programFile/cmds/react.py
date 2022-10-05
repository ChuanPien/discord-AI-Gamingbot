import discord, json
from time import sleep
from discord.ext import commands
from core.classes import Cog_Extension,Global_Data
import WIP_other_porgram
# from WEB_REQUESTS.testPOEweb import testPOE


with open('./poe_json/ID_fix.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

class React(Cog_Extension):
    @commands.command()
    async def test(self, ctx, arg):
        await ctx.send(arg)
#測試用指令
    @commands.command()
    async def hi(self, ctx):
        print("HI!~")
        await ctx.send("ABCC")
    '''
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
    '''

    # poe.ninja簡易查詢
    @commands.command()
    async def poesearch(self, ctx, *,msg):
        Wop =""
        if msg == 'help':
            # skill:fire-trap-support:item:skillmode:keystone:allskill(代翻):weapon
            await ctx.send(f'此指令使用方法: 若該格無查詢目標則留空\n`poesearch 【主技能:副技能:道具:技能模式:keystone:全技能:武器】')
        else:
            Wop = WIP_other_porgram.test(msg)
        await ctx.send(Wop.ninja())
    
    # 詞墜表單測試
    @commands.command()
    async def shlist(self, ctx):
        typeteam = []
        count = 0
        msglline = 0
        for typelist in jdata['詞墜']:
            if count < 3:
                typeteam.append(typelist)
                count = count + 1
            elif count == 3:
                msglline = msglline + (count/3)
                await ctx.send(typeteam)
                count = 0
                typeteam = []
            if msglline == 3:
                sleep(1)
                msglline = 0
        else:
            await ctx.send(typeteam)
    

def setup(bot):
    bot.add_cog(React(bot))