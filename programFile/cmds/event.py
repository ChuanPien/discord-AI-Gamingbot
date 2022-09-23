import discord
import json
import datetime # 引入datetime
from discord.ext import commands
from cmds.owner import Owner
from core.classes import Cog_Extension,Global_Func,messageFormat
from time import sleep


#打開json並讀取，使用utf8 encode
with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)


class Event(Cog_Extension):
    @commands.Cog.listener()
    #on_massage功能必須寫在同一處 不然會覆蓋
    async def on_message(self, msg):
        # 開頭原始訊息站存
        msg_content = ""
        # 關鍵字列表
        msg_prokey = ['Test','test']
        #設定傳送消息頻道
        sendContentChannel = self.bot.get_channel(jdata['Trans_channelID'])
        #初始化，設定專用log頻道
        logChat = self.bot.get_channel(jdata['Log_chat'])
        #msg抓取初始化
        if msg.author != self.bot.user:
            msgFormat = msg.content
            msgFormat = msgFormat.split(" ")
            msg_content = msgFormat[0]
            print(msgFormat,msg_content)
        #測試用指令
        if msg.content == 'Test' or msg.content == 'test' and msg.author != self.bot.user and msg.author.name == "must505":
            await msg.channel.send('Hello!')

        if msg_content == 'poesearch' 
        #測試log運作
        if msg.author != self.bot.user:
            for mf in msgFormat:
                if mf == 'sec' :
                #debug
                    await msg.channel.send("log運作測試")
                    #初始化messageFormat
                    msg_f = messageFormat(msg)
                    msg_f.log()
                    await logChat.send("－－－－－\n"+"ID: "+msg_f.getUserId()+"\nMsg: "+msg_f.getMsg()+"\n－－－－－")
                else:
                    print("非關鍵字 & 錯誤頻道，不記錄訊息")
                    break
            
        #傳送A群組文字頻道消息到B群組
        if msg.channel.id == jdata['listen_channelID'] or msg.channel.id == jdata['listen_test_channelID'] and msg.author != self.bot.user:
            #Debug
            #print(f'Fetched message: {msg}')
            #discord.Client.sniped_message = msg
            """ 老格式
            await sendContentChannel.send("－－－－－－－－－－－－"+Global_Func.getTime()+"－－－－－－－－－－－－")
            sleep(1)
            await sendContentChannel.send("訊息 : " + str(msg.content))
            sleep(0.5)
            if msg.author.nick == None:
                await sendContentChannel.send("訊息發送者 : " + str(msg.author.name))
            else:
                await sendContentChannel.send("訊息發送者(伺服器暱稱) : " + str(msg.author.nick))
            sleep(1)
            await sendContentChannel.send("訊息發送頻道 : "+ str(msg.channel.name)+" ,"+str(msg.channel.id))
            sleep(0.5)
            await sendContentChannel.send("訊息伺服器 : "+ str(msg.author.guild.name))
            sleep(1)
            await sendContentChannel.send("－－－－－－－－－－－－－－－－－－－－－－－－－")
            """
            if msg.author.nick == None:
                await sendContentChannel.send("－－－－－－－－－－－－"+Global_Func.getTime()+"－－－－－－－－－－－－"+Global_Func.logMessage(msg,0,1,1,1,1,0)+"\n－－－－－－－－－－－－－－－－－－－－－－－－－")
            else:
                await sendContentChannel.send("－－－－－－－－－－－－"+Global_Func.getTime()+"－－－－－－－－－－－－"+Global_Func.logMessage(msg,1,1,1,1,1,0)+"\n－－－－－－－－－－－－－－－－－－－－－－－－－")

        if msg.channel.id == 995880772227567726 and msg.author.name == "must505" and msg.content == "list":
            for name in jdata:
                sleep(1.5)
                await msg.channel.send(name)
                print(name)


    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        #初始化，設定專用log頻道
        channel_log = self.bot.get_channel(jdata['Del_chat_log_ID'])
        endShow = 0
        if msg.author.guild.name != str(jdata['test_discord_group']):
            #在cmd上記錄，並顯示時間
            print("wrong group! don't do anything    "+Global_Func.getTime())
            #await channel_log.send("wrong group! don't do anything")
        else:
            #顯示時間
            await channel_log.send("----------------"+ Global_Func.getTime() + "-------------------")
            #抓取審核日誌 並提取刪除操作人 發出消息到專用頻道
            counter = 1
            async for audilog in msg.guild.audit_logs(action = discord.AuditLogAction.message_delete):
                if counter == 1:
                    await channel_log.send("刪除者(discord名子) : " + str(audilog.user.name))
                    #debug
                    #await channel_log.send("Test see" + str(audilog))
                    counter +=1
            sleep(1)
            #發送刪除消息到 專用頻道
            """ old version send
            await channel_log.send("原始訊息內容 : " + str(msg.content))
            sleep(1)
            await channel_log.send("原始訊息頻道 : " + str(msg.channel.name))
            sleep(3)
            await channel_log.send("原始訊息頻道ID : "+ str(msg.channel.id))
            sleep(1)
            await channel_log.send("原始訊息群組 : " + str(msg.author.guild.name))
            sleep(1)
            if msg.author.nick != None:
                await channel_log.send("原始訊息發送者(伺服器暱稱) : " + str(msg.author.nick))
            sleep(1)
            await channel_log.send("原始訊息發送者(真實ID) : " + str(msg.author.name))
            """
            #new version send
            await channel_log.send(Global_Func.logMessage(msg,1,1,1,1,1,0))
            #debug
            #await channel_log.send("Test see2" + str(msg))
            endShow +=1
        #訊息結尾
        #print(endShow)
        if endShow != 0:
            sleep(1)
            await channel_log.send("\n----------------Delete Log End -------------------")
    







def setup(bot):
    bot.add_cog(Event(bot))
