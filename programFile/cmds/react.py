import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
from WEB_REQUESTS.msgFormat import messageFormat as msg_f

#打開json並讀取，使用utf8 encode
with open('setting.json',mode='r',encoding='utf8') as jFile:
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
    @commands.command()
    async def log(self, ctx):
        #初始化，設定專用log頻道
        logChat = self.bot.get_channel(jdata['Log_chat'])
        text = ctx
        id = ctx.author.id
        msg_f(text,id)
        await logChat.send("ID: "+msg_f.getUserId()+"\nMsg: "+msg_f.getMsg())
        

def setup(bot):
    bot.add_cog(React(bot))