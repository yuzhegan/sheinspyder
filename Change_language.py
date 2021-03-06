# encoding='utf-8

# @Time: 2021-12-28
# @File: %
#!/usr/bin/env
from icecream import ic
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains包



class Change_language():

    """Docstring for Change_language. """

    def load(self, brower, url):
        if brower != None and url != "":

            # brower.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                # "source": """
                # Object.defineProperty(navigator, 'webdriver', {
                  # get: () => undefined
                # })
              # """

            # })
            brower.get(url)
            # time.sleep(3)

            # 等待弹窗, 点击关闭按钮
            try:
                WebDriverWait(brower, 10).until(EC.presence_of_element_located(
                  (By.CLASS_NAME, "c-coupon-box")))
                brower.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/i").click()
                # time.sleep(3)
            except Exception as e:
                print(e)

            # 切换语言为日语 点击语言列表
            ele = brower.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[5]/a/span/i")
            ActionChains(brower).move_to_element(ele).perform() #让鼠标悬停在ele上
            # brower.find_element_by_xpath("//div[2]/div[1]/div/div[1]/div/div[3]/div[5]/a/span/i").click()
            # time.sleep(1)
            brower.find_element_by_xpath("//div[2]/div[1]/div/div[1]/div/div[3]/div[5]/div/div[4]/a[2]").click()
            # time.sleep(3)


# if __name__ =="__main__":
    # url = "https://jp.shein.com/DAZY-Solid-Cable-Knit-Drop-Shoulder-Sweater-p-5835597-cat-1734.html?scici=WomenHomePage~~ON_Banner,CN_category,HZ_Knitwear,HI_hotZoneuadal3wddc8~~6_1~~real_2216~~~~"
    # a = Change_language()
    # a.load(url)
