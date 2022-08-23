import requests

if __name__== "__main__":
    url = 'https://www.google.com/'

    reponse = requests.get(url=url)

    page_text = reponse.text
    print(page_text)

    with open('./google.html','w',encoding='utf-8') as fp:
        fp.write(page_text)

    print('craw end')