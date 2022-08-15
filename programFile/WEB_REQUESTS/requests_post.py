import requests
from time import sleep
import json

if __name__== "__main__":
    with open('query.json',mode='r',encoding='utf8') as jFile:
        jdata = json.load(jFile)
    #sleep(5)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '118',
        'Content-Type': 'application/json',
        'Cookie': '_ga=GA1.2.1222773361.1658121743; stored_data=1; POESESSID=d06178e937205232066827d96b54ba76; _gid=GA1.2.1237697955.1660530539; _gat=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
    }
    post_url = "https://web.poe.garena.tw/api/trade/search/守望聯盟"
    test_url = "https://www.pathofexile.com/api/trade/search/Standard"
    data = jdata
    reponse=requests.post(url=post_url,data=data,headers=headers)
    reasonPost = reponse.reason
    start = reponse.status_code
    
    #reponse.json() 取得交易頁面數據用
    #reponse = reponse.json()
    print(str(reasonPost))
    print("code:" +str(start))
    #print("reponse : "+str(reponse))
    print(reponse.text)
