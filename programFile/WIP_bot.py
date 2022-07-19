# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import discord
import json
from discord.ext import commands
import os
import ttt

#打開json並讀取，使用utf8 encode
with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

client = discord.Client()
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('>>>  Bot Is online <<<')
    print('We have logged in as {0.user}'.format(bot))
    

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"RE-Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"un-Loaded {extension} done.")

@bot.command()
async def search(ctx, msg):
    t = ttt.test(msg)
    print(t.google())
    await ctx.send(t.google())

for filename in os.listdir("./cmds"):
    if filename.endswith('.py'):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata['Token'])
