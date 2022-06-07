# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTgzNjA0Nzc4MjAwMzY3MTA0.GBBTjV.R6-so8-gNEVlZU_E76KKw6crKQ20KiZ-psxUUE')
