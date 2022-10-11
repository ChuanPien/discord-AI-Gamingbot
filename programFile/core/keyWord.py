import discord
import json
from discord.ext import commands

# 打開json並讀取，使用utf8 encode
with open('setting.json', mode='r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

