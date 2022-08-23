import requests

#UA : user-Agent (請求裝置的身分編號)
#偽裝UA :爬蟲的對應請求裝置身分編號，將其偽裝成某遊覽器


if __name__== "__main__":
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
    }
    url='https://www.google.com/search?q='
    #整理url附帶的參數: 包裝到字典
    kw =input('enter a word: ')
    param = {
        'query':kw
    }
    #對指定url發送的請求對應的url是附帶參數的,並且請求過程中處理了參數
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text

    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)

