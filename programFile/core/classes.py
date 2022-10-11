import discord
from discord.ext import commands
import datetime
import json

class Cog_Extension(commands.Cog):
    #用於Cog繼承
    def __init__(self,bot):
        self.bot = bot

class Global_Func():
    #自定義常用功能

    #取得現在時間
    def getTime():
        return str(datetime.datetime.now())


class messageFormat():
    #訊息格式化
    def __init__(self,msg):
        self.msg = str(msg.content)
        self.usersId = str(msg.author.id)
    def getMsg(self):
        return str(self.msg)
    def getUserId(self):
        return str(self.usersId)
    def log(self):
        users = str(str(self.usersId)+"-"+Global_Func.getTime())
        print("\n\n users : ",users)
        newData = {users:self.msg}
        #初始化jdata,jsonNull
        jdata = {}
        jsonNull = False
        with open('log.json','r',encoding='utf8') as jFile:
            jread = jFile.read()
            if jread == "":
                print("\n\n\njdata是空的!")
                jdata = {}
                jdata.update(newData)
            else:
                jsonNull = True
                jFile.close()
        if jsonNull == True:
            with open('log.json','r',encoding='utf8') as jFile:
                jdata = json.load(jFile)
                print("\n\n  : ",jdata)
                #jdata["{}".format(self.data)].append(self.text)
        jdata.update(newData)
        print("\n\n jdata-append : ",jdata)
        with open('log.json','w',encoding='utf8') as jFile:
            json.dump(jdata,jFile, indent=4, ensure_ascii=False)
        print("\n\n jFile : ",jFile)
        jFile.close()
        print("完成瞜~")
    def msgsp():
        pass