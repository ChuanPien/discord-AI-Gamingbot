

class test:
    def __init__(self, search):
        self.search = search
    def google(self):
        #.replace(" ","+") 將空白字元轉換成google網址的空白搜尋替代字元
        #以便正確顯示搜尋的相關網址
        google = "https://www.google.com/search?q="+str(self.search.replace(" ","+"))
        return google
    def ninja(self):
        testString = self.search.split(":")
        skill = "?skill="+testString[0]
        item = "item="+testString[1]
        skillmode = "skillmode="+testString[2]
        keystone = "keystone="+testString[3]
        allskill = "allskill="+testString[4]
        weapon = "weapon="+testString[5]


        poe = "https://poe.ninja/challenge/builds"+skill+"&"+item+"&"+skillmode+"&"+keystone+"&"+allskill+"&"+weapon
        return poe

