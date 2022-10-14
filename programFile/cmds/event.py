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
        if msg.author != self.bot.user:
            pass


def setup(bot):
    bot.add_cog(Event(bot))
