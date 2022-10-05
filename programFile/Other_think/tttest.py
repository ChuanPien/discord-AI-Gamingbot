from time import sleep
import ttt

sch = "123 456 7864 5a4s6d54a5 4a6s 4a56s 4d6a4s"
sch.replace(" ","+")
msg = "流派"

testStringType = "a54s5d45as5da 詞墜 保險箱 "

#t = ttt.test(msg)
#print("1 : "+sch+" \n2 : "+t.google())

#t.ninja()

import json
#打開json並讀取，使用utf8 encode
with open('ID_fix.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)
print(type(jdata))
#print(jdata['詞墜'])
listec = []
liste = []
count = 0
msglline = 0
for str in jdata['詞墜']:
    if count < 3:
        liste.append(str)
        #print(str)
        count = count + 1
    elif count == 3:
        msglline = msglline + (count/3)
        listec = listec + liste
        print(liste)
        count = 0
        liste = []
    if msglline == 3:
        sleep(0.001)
        msglline = 0
print(listec)

print(f"大分類數量: {len(listec)}")


indexDict = listec.index(input('>'))
print(f"\n\n\n\n{jdata['詞墜'][listec[indexDict]]} \n\n\n 總數{len(jdata['詞墜'][listec[indexDict]])}")

#del jdata['id']
'''
jsonlist = jdata.split('/n')
for str in jsonlist:
    for strlay2 in jsonlist['詞墜']:
            print(strlay2)'''







'''
proKey = jdata["詞墜"]
count_testStringType = 0
list_testStringType = testStringType.split(" ")

print(len(list_testStringType))
print(list_testStringType)

if set(list_testStringType) & set(proKey):
    t = ttt.test(testStringType)
    print(t.ninja())
else:
    print("Fail")


print("元素檢查")
print(list_testStringType.index('元素抗性'))
'''

    

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