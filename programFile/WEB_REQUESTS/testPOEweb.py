from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from core.classes import Global_Data

##
## '無'屬性/輸入錯誤 修改
##
class testPOE():
    def __init__(self,item,lvls):
        self.item = item
        self.lvls = lvls
    def chromedriver(self):
        PATH = "D:/ChromeDriver/chromedriver.exe"
        gd = Global_Data()
        #item輸入
        item = self.item
        #詞墜輸入
        lvls = self.lvls
        gd.search_reactMsg = "裝備:"+item,"\n屬性:",lvls

        driver = webdriver.Chrome(PATH)
        driver.get("https://poedb.tw/tw/Modifiers")

        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "py-1"))
        )

        item = driver.find_element(By.LINK_TEXT, item)
        action = ActionChains(driver).click(item).perform()

        time.sleep(1.5)

        for lvl in lvls:
            titles = driver.find_elements(By.CLASS_NAME, "inline-block")
            for title in titles:
                if title.text == lvl:
                    action3 = ActionChains(driver).click(title).perform()
                    break

# lvls.clear()
