# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import discord

#intents = 

client = discord.Client()

@client.event
async def on_ready():
    print('>>>  Bot Is online <<<')
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('查詢'):
        await message.channel.send('Done!')

client.run('OTgzNjA0Nzc4MjAwMzY3MTA0.GH3rLL.T-mv9IvdZRd2U1Mgp_-tU5MZfUptkwzaDhlGIc')
