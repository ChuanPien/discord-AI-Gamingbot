import discord
from discord.ext import commands
import datetime

class Cog_Extension(commands.Cog):
    #用於Cog繼承
    def __init__(self,bot):
        self.bot = bot

class Global_Func():
    #自定義常用功能

    #取得現在時間
    def getTime():
        return str(datetime.datetime.now())
    #msg訊息發送選擇
    def logMessage(msg,authorNick,authorName,guildName,chatName,chatId,guildMembers):
        msgJson = [authorNick,authorName,guildName,chatName,chatId,guildMembers]
        msgSendNick = "\n訊息發送者(伺服器暱稱) : " + str(msg.author.nick)
        msgSendName = "\n訊息發送者 : " + str(msg.author.name)
        msgContent = "\n訊息 : " + str(msg.content)
        authorGuildName = "\n訊息伺服器 : "+ str(msg.author.guild.name)
        channelName = "\n訊息頻道 : " + str(msg.channel.name)
        channelId = "\n訊息頻道ID : "+ str(msg.channel.id)
        memberCount = "\n成員數 : "+ str(msg.author.guild.member_count)
        printList = [msgSendNick,msgSendName,msgContent,authorGuildName,channelName,channelId,memberCount]
        returnText = ""
        for lists in range(len(msgJson)):
            if msgJson[lists] != 1:
                continue
            returnText = returnText+str(printList[lists])
        return returnText