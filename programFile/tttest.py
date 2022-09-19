import ttt
sch = "123 456 7864 5a4s6d54a5 4a6s 4a56s 4d6a4s"
sch.replace(" ","+")
msg = "Anomalous-Forbidden-Rite,Vaal-Cyclone:Aegis-Aurora:Normal:Malediction:Cyclone:Claw-/-Shield"
t = ttt.test(msg)
#print("1 : "+sch+" \n2 : "+t.google())
t.ninja()

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