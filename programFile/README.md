# 給組員
存放、共同編輯程式的資料夾。

# 本程式的編成環境
Python 3.9.7

## 使用的主要python模組(module)與其他檔案類型
- module
    1. discord.py----1.7.3
    2. thefuzz----0.19.0
- filesType
    1. json

> 一定要安裝1.7.3版本的discord.py才可運行,1.7.3以上的版本官方大改,如需要請至官方文檔觀看並修改程式碼方便執行

## 使用方法
1. 將其python環境與discord.py安裝完畢,並且各版本虛相同
2. 下載此專案中的programFile資料夾內容
3. 更改其中official_setting.json文件名為**setting.json**,並自行修改其中內容
4. 運行其WIP_bot.py/bot.py
5. Enjoy

## 結構說明

### /cmds旗下檔案
event.py 為各種觸發事件
main.py 為主要的功能
owner.py 為**擁有者/作者**專用指令集
react.py 為反應類型功能

### /core旗下檔案
classes.py 負責存放**必要的模塊**(如Cog)與**常用功能**
也可自行新增其他程式於此


### /README.md
就是你看到的本篇內容,專為此資料夾解說

### /official_setting.json
各類設定檔,包含啟動bot的專屬碼
**但此為範本**,請根據自行需求更改
**務必注意不要將bot啟動碼公開!**
**務必注意不要將bot啟動碼公開!**
**務必注意不要將bot啟動碼公開!**

