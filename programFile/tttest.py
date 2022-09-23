from itertools import count
import ttt

sch = "123 456 7864 5a4s6d54a5 4a6s 4a56s 4d6a4s"
sch.replace(" ","+")
msg = "流派"

testStringType = "a54s5d45as5da poeser "

#t = ttt.test(msg)
#print("1 : "+sch+" \n2 : "+t.google())

#t.ninja()

import json
#打開json並讀取，使用utf8 encode
with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)
proKey = jdata["proKey"]
count_testStringType = 0
list_testStringType = testStringType.split(" ")

print(len(list_testStringType))

if set(list_testStringType) & set(proKey):
    t = ttt.test(testStringType)
    print(t.ninja())
else:
    print("Fail")

print("元素檢查")
print(list_testStringType.index('派系'))


    

"""
字串與list字串空值檢測 紀錄

testStringType = testStringType.split(":")
#testStringType = testStringType.split(":")
print(testStringType)
for i in range(0,len(testStringType)):
    stringContent = testStringType[i]
    if stringContent == '':
        pass
    else:
        print(f'{i} = {stringContent}\n type = {type(testStringType[i])}')


skill=Anomalous-Forbidden-Rite,Vaal-Cyclone
&item=Aegis-Aurora,Impossible-Escape
&weapon=Claw-/-Shield
&allskill=Cyclone
&keystone=Malediction
&skillmode=Normal





"""

"""
        msgJson = [authorNick,authorName,guildName,chatName,chatId,guildMembers]
        msgSendNick = msg.author.nick
        msgSendName = msg.author.name
        msgContent = msg.content
        authorGuildName = msg.author.guild.name
        channelName = msg.channel.name
        channelId = msg.channel.id
        memberCount = msg.author.guild.member_count
        printList = [msgSendNick,msgSendName,msgContent,authorGuildName,channelName,channelId,memberCount]
        for lists in range(len(msgJson)):
            if msgJson != 1:
                continue
            print
"""