

class test:
    def __init__(self, search):
        self.search = search
    def google(self):
        #.replace(" ","+") 將空白字元轉換成google網址的空白搜尋替代字元
        #以便正確顯示搜尋的相關網址
        google = "https://www.google.com/search?q="+str(self.search.replace(" ","+"))
        return google
    def ninja(self):
        # 初始化 第一元素值
        first_element = 0
        # 初始化最終url
        last_url =''
        # 初始化流派(poe.ninja)url
        url_ninja = 'https://poe.ninja/challenge/builds?'
        # 建立元素列表
        url_element = ["skill=","item=","skillmode=","keystone=","allskill=","weapon="]
        # 建立元素連接符號
        element_link = "&"
        # 分割使用者輸入文字
        user_input = self.search.split(":")

        for i in range(0,len(user_input)):
            stringContent = user_input[i]
            if stringContent == '':
                pass
            elif first_element == 0:
                last_url = url_ninja+url_element[i]+stringContent
                first_element = first_element + 1
            elif first_element != 0:
                last_url = last_url+element_link+url_element[i]+stringContent
            else:
                last_url = "輸出錯誤"
                break
            
        return last_url

