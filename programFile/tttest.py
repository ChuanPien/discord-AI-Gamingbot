from matplotlib import test
import ttt
sch = "123 456 7864 5a4s6d54a5 4a6s 4a56s 4d6a4s"
sch.replace(" ","+")
msg = "::::"

testStringType = "123456:::asdasd:"

t = ttt.test(msg)
#print("1 : "+sch+" \n2 : "+t.google())

t.ninja()


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