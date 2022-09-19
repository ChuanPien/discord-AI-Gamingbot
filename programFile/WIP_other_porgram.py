

class test:
    def __init__(self, search):
        self.search = search
    def google(self):
        #.replace(" ","+") 將空白字元轉換成google網址的空白搜尋替代字元
        #以便正確顯示搜尋的相關網址
        google = "https://www.google.com/search?q="+str(self.search.replace(" ","+"))
        return google
    def ninja(self):
        poe = "https://poe.ninja/challenge/builds"+str(self.search.replace(" ","&"))
        return poe

"""
https://poe.ninja/challenge/builds
?skill= string,string2.....
?item = 同上
?skillmode = 同上
?keystone =同上
?allskill=
?weapon =同上
多重條件連結用&
"""