import requests
from time import sleep
import json

if __name__== "__main__":
    with open('query.json',mode='r',encoding='utf8') as jFile:
        jdata = json.load(jFile)
    sleep(5)
    headers = {
        Accept: */*,
        Accept-Encoding: gzip, deflate, br,
        Accept-Language: zh-TW,zh;q=0.9,
        Connection: keep-alive,
        Content-Length: 118,
        Content-Type: application/json,
        Cookie: POESESSID=ccbd59dbab4ed0c727692ed1bec70926,
        Host: web.poe.garena.tw,
        Origin: https://web.poe.garena.tw,
        Referer: https://web.poe.garena.tw/trade/search/%E5%AE%88%E6%9C%9B%E8%81%AF%E7%9B%9F,
        sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103",
        sec-ch-ua-mobile: ?0,
        sec-ch-ua-platform: "Windows",
        Sec-Fetch-Dest: empty,
        Sec-Fetch-Mode: 'cors',
        Sec-Fetch-Site: 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        'X-Requested-With': 'XMLHttpRequest'
    }
    post_url = "https://web.poe.garena.tw/api/trade/search/守望聯盟"
    test_url = "https://www.pathofexile.com/api/trade/search/Standard"
    data = jdata
    reponse = requests.post(url=test_url,data=data,headers=headers)
    reasonPost = reponse.reason
    start = reponse.status_code
    
    #reponse.json() 取得交易頁面數據用
    #reponse = reponse.json()
    print(str(reasonPost))
    print("code:" +str(start))
    #print("reponse : "+str(reponse))
    print(reponse.text)
