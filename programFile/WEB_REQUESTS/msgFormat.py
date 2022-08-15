import json
class messageFormat():
    def __init__(self,msg,usersId):
        self.msg = msg
        self.usersId = usersId
    def getMsg(self):
        return str(self.msg)
    def getUserId(self):
        return str(self.usersId)
    def log(self):
        newData = {self.usersId:self.msg}
        with open('log.json','r',encoding='utf8') as jFile:
            jdata = json.load(jFile)
            jdata.update(newData)
        jFile.close()
        with open('log.json','w',encoding='utf8') as jFile:
            json.dump(newData,jFile)
        jFile.close()
    