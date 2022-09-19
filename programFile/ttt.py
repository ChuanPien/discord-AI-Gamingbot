import os 
import json
import datetime

#for filename in os.listdir('./cmds'):
#    print(filename)

#import datetime # 引入datetime
#nowTime = datetime.datetime.now() # 取得現在時間
#print(nowTime)

#with open('setting.json',mode='r',encoding='utf8') as jFile:
#    jdata = json.load(jFile)

#msg = "Trans_channelID"
#for jdata in jdata:
#        print(jdata)

class test:
    def __init__(self, search):
        self.search = search
    def getTime():
        print (str(datetime.datetime.now()))
    def google(self):
        searche = self.search
        searche.replace(" ","%20")
        print(searche)
        google = "https://www.google.com/search?q="+str(searche)
        return google
    #msg訊息發送選擇
    def logMessage(self,authorNick,authorName,guildName,chatName,chatId,guildMembers):
        list = []
        list.append(authorNick)
        list.append(authorName)
        list.append(guildName)
        list.append(chatName)
        list.append(chatId)
        list.append(guildMembers)
        msg = [123,test.append(456),789,132,465,798]
        test = []
        for lists in range(len(list)):
            #print(f"lists : {lists}")
            if list[lists] !=1:
                #print("list :"+str(list[lists]))
                continue
            print("msg : "+str(msg[lists]))
    def ninja(self):
        testString = self.search.split(":")
        skill = "?skill="+testString[0]
        item = "item="+testString[1]
        skillmode = "skillmode="+testString[2]
        keystone = "keystone="+testString[3]
        allskill = "allskill="+testString[4]
        weapon = "weapon="+testString[5]


        poe = "https://poe.ninja/challenge/builds"+skill+"&"+item+"&"+skillmode+"&"+keystone+"&"+allskill+"&"+weapon
        #print('1. {}, 2. {} 3. {} 4. {} 5. {} 6.{} '.format(skill,item,skillmode,keystone,allskill,weapon))
        print(poe)





"""
https://poe.ninja/challenge/builds
?skill= string,string2.....
?item = 同上
?skillmode = 同上
?keystone =同上
?allskill=
?weapon =同上
多重條件連結用&
不同查詢條件使用:作區別,進程式後依照:切割條件,使用&做個別條件合併
&合併後面的條件不需要以?作為前墜,?xxxx取代成&xxxx
"""


"""

格式研究

<Message id=996261150511595539 

    channel=
        <TextChannel id=995880772227567726 
        name='bot_test_char' 
        position=6 
        nsfw=False 
        news=False 
        category_id=995880667697131612
        > 
    type=
        <MessageType.default: 0
        > 
    author=
        <Member id=968372079713996821 
        name='must505' 
        discriminator='3427' 
        bot=False 
        nick='我就爛(the沈）' 
        guild=
            <Guild id=915155098827644972 
            name='專題' 
            shard_id=None 
            chunked=False 
            member_count=6
            >
        > 
    
    flags=<MessageFlags value=0>
    >
msg.author.nick sv暱稱
msg.author.name real名
msg.content 內容
msg.author.guild.name sv名
msg.channel.name 頻道名
msg.channel.id 頻道id
msg.author.guild.member_count 成員數

Test see<
        AuditLogEntry id=996268962948075560 
        action=AuditLogAction.message_delete 
        user=<
                User id=968372079713996821 
                name='must505' 
                discriminator='3427' 
                bot=False>>



Fetched message: <
                    Message id=998418355352518686 
                    channel=<
                            TextChannel id=998399920799219854 
                            name='bot搬移聊天紀錄' 
                            position=5 
                            nsfw=False 
                            news=False 
                            category_id=998399920321089561
                            > 
                    type=<
                        MessageType.default: 0
                        > 
                    author=<
                        Member id=968372079713996821 
                        name='must505' 
                        discriminator='3427' 
                        bot=False 
                        nick=None 
                        guild=<
                            Guild id=998399920321089556 
                            name='must505 的伺服器' 
                            shard_id=None 
                            chunked=False 
                            member_count=2
                            >
                        > 
                    flags=<MessageFlags value=0>>
Fetched message.(id channel type author flags).(id name ....).(id name.....)

"""