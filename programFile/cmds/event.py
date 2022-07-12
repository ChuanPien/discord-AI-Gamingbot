import discord
import json
import datetime # 引入datetime
from discord.ext import commands
from core.classes import Cog_Extension
from time import sleep




#打開json並讀取，使用utf8 encode
with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'Test' and msg.author != self.bot.user:
            await msg.channel.send('Hello!')
        
        if msg.content == '查詢' and msg.author != self.bot.user:
            await msg.channel.send('Test Done!')

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        #初始化專用頻道
        channel_log = self.bot.get_channel(jdata['Del_chat_ID'])
        await channel_log.send("----------------"+ str(datetime.datetime.now()) + "-------------------")
        #抓取審核日誌 並提取刪除操作人 發出消息到專用頻道
        counter = 1
        async for audilog in msg.guild.audit_logs(action = discord.AuditLogAction.message_delete):
            if counter == 1:
                await channel_log.send("who del : " + str(audilog.user.name))
                #await channel_log.send("Test see" + str(audilog))
                counter +=1
        sleep(1)
        #發送刪除消息到 專用頻道
        await channel_log.send("This msg content : " + str(msg.content))
        sleep(1)
        await channel_log.send("from where the chat : " + str(msg.channel.name))
        sleep(1)
        if msg.author.nick != None:
            await channel_log.send("who send(nickName) : " + str(msg.author.nick))
        sleep(1)
        await channel_log.send("Send This Msg ID(turnName) : " + str(msg.author.name))
        #await channel_log.send("Test see2" + str(msg))
        await channel_log.send("---------------- End -------------------")
    
    









def setup(bot):
    bot.add_cog(Event(bot))
