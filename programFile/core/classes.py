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
    