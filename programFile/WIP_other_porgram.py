

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
        # 使用者輸入空字串計數器
        input_list_none_count = 0
        # 初始化最終url
        last_url = None
        # 初始化流派(poe.ninja)url
        url_ninja = 'https://poe.ninja/challenge/builds?'
        # 建立元素列表
        url_element = ["skill=","fire-trap-support=","item=","skillmode=","keystone=","allskill=","weapon="]
        # 建立元素連接符號
        element_link = "&"
        # 分割使用者輸入文字
        user_input = self.search.split(":")

        # debug
        print(f'input = {user_input},{len(user_input)}')

        # 迴圈檢查input並輸出對應結果
        if len(user_input) == len(url_element):
            for i in range(0,len(url_element)):
                stringContent = user_input[i]
                # 如果空值則讓計數器增加
                if stringContent == '':
                    input_list_none_count += 1
                # 不是空值且是第一個條件
                elif stringContent != '' and first_element == 0:
                    last_url = url_ninja+url_element[i]+stringContent
                    # 第一條件計數器+1
                    first_element = first_element + 1
                # 非第一條件時合併其他條件
                elif stringContent != '' and first_element != 0:
                    last_url = last_url+element_link+url_element[i]+stringContent
                else:
                    last_url = "輸出錯誤"
                    print(input_list_none_count)
                    break
        else:
            last_url = "錯誤的格式或其他未知錯誤"
        if input_list_none_count == len(user_input):
            last_url = "請至少輸入一項查詢項目"
            
        return str(last_url)

