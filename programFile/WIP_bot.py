# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import discord
import json
from discord.ext import commands
import os
import WIP_other_porgram

#打開json並讀取，使用utf8 encode
with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

client = discord.Client()
bot = commands.Bot(command_prefix=jdata['Prefix'],owner_ids=jdata['Owner_id'])

#啟動完成發送，bot上線消息(cmd)
@bot.event
async def on_ready():
    print('>>>  Bot Is online <<<')
    print('We have logged in as {0.user}'.format(bot))

#bot關閉後，發送訊息至cmd
@bot.event
@bot.is_owner()
async def on_close():
    print('>>>  Bot Is offline <<<')
    
#簡易google查詢
@bot.command()
async def search(ctx, *,msg):
    Wop = WIP_other_porgram.test(msg)
    print(Wop.google())
    await ctx.send(Wop.google())

#load cmds資料夾內所有cog
for filename in os.listdir("./cmds"):
    if filename.endswith('.py'):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata['Token'])
