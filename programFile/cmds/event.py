import discord
import json
import datetime  # 引入datetime
from discord.ext import commands
from core.classes import Cog_Extension, Global_Func, messageFormat
from time import sleep

# 打開json並讀取，使用utf8 encode
with open('setting.json', mode='r', encoding='utf8') as jFile:
    jdata = json.load(jFile)


class Event(Cog_Extension):
    @commands.Cog.listener()
    # on_massage功能必須寫在同一處 不然會覆蓋
    async def on_message(self, msg):
        # 設定傳送消息頻道
        sendContentChannel = self.bot.get_channel(jdata['listen_test_channelID'])
        # 初始化，設定專用log頻道
        logChat = self.bot.get_channel(jdata['Log_chat'])
        # msg抓取初始化
        if msg.author != self.bot.user:
            msgFormat = msg.content
            msgFormat = msgFormat.split(" ")
            print(msgFormat)

        # 測試log運作
        if msg.author != self.bot.user:
            for mf in msgFormat:
                if mf == 'sec':
                    # debug
                    await msg.channel.send("log運作測試")
                    # 初始化messageFormat
                    msg_f = messageFormat(msg)
                    msg_f.log()
                    await logChat.send("－－－－－\n" + "ID: " + msg_f.getUserId() + "\nMsg: " + msg_f.getMsg() + "\n－－－－－")
                else:
                    print("\n\nError")
        


def setup(bot):
    bot.add_cog(Event(bot))
