import asyncio
import json
import os

from discord.ext import commands

from core.classes import Cog_Extension

# @commands.is_owner() >> 辨別是否為擁有者
# 打開json並讀取，使用utf8 encode
with open('setting.json', mode='r', encoding='utf8') as jFile:
    jdata = json.load(jFile)


class Owner(Cog_Extension):
    # load模塊(Cog)
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.bot.load_extension(f"cmds.{extension}")
        await ctx.send(f"Loaded {extension} done.")

    # reload模塊(Cog)
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        if extension == "*":
            # load cmds資料夾內所有cog
            for filename in os.listdir("./cmds"):
                if filename.endswith('.py'):
                    self.bot.reload_extension(f"cmds.{filename[:-3]}")
            await ctx.send(f"RE-Loaded ALL done.")
        else:
            self.bot.reload_extension(f"cmds.{extension}")
            await ctx.send(f"RE-Loaded {extension} done.")

    # unload模塊(Cog)
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f"cmds.{extension}")
        await ctx.send(f"un-Loaded {extension} done.")

    # close bot
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Shutdown now..... Pls wait")
        await asyncio.sleep(1)
        await self.bot.close()

    # 測試用指令
    @commands.command()
    async def hi(self, ctx):
        print("HI!~")
        await ctx.send("我在喔~")

    # 取得使用此指令的頻道ID
    @commands.command()
    @commands.is_owner()
    async def getchid(self, ctx):
        await ctx.send(f'This Chennel ID is : {ctx.channel.id}')

    # 取得使用指令的使用者ID
    @commands.command()
    @commands.is_owner()
    async def myid(self, ctx):
        await ctx.send(f'Your ID is : {ctx.author.id}')

    # 對特定頻道傳送消息
    # ID必須為整數型態
    @commands.command()
    @commands.is_owner()
    async def chmsg(self, ctx, text, getid):
        userid = ctx.author.nick
        sendmsgch = self.bot.get_channel(int(getid))
        await sendmsgch.send(f'{userid} 說 : {text}')


def setup(bot):
    bot.add_cog(Owner(bot))
