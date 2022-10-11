
import os 
import json
from thefuzz import fuzz
from thefuzz import process


ID_Dict = {}
with open('ID_fix.json', mode='r', encoding='utf8') as jFile:
    jdata = json.load(jFile)
    ID_Dict = jdata

#print(ID_Dict['詞墜']['normal'])

returnList = []
inputS = input("詞墜:\n> ")
typeID = input("查看詞墜分類:\n> ")

for str in ID_Dict:
    for str2 in ID_Dict[str]:
        for textstr in ID_Dict[str][typeID]:
            # 使用thefuzz moudle判斷是否有類似的詞墜
            point = fuzz.token_set_ratio(textstr['text'],inputS)
            print(textstr)
            # 如果有(結果不是0),就加入至新list
            if point != 0:
                returnList.append(textstr['text'])

print(returnList,len(returnList))




#ser = fuzz.token_sort_ratio(ID_Dict, ID_Dict)

#print(ser)





