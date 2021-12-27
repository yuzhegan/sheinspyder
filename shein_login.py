# encoding='utf-8

# @Time: 2021-12-25
# @File: %
#!/usr/bin/env
from icecream import ic
import time
from selenium import webdriver
import json
import os
import requests

brower = webdriver.Chrome(executable_path="/home/dav/Downloads/chromedriver")
login_url = "https://jp.shein.com/user/auth/login"
def getSheinCookies():
    # get login taobao cookies
    brower.get(login_url)
    while True:
        print("Please login in shein.com!")
        time.sleep(3)
        # if login in successfully, url  jump to www.taobao.com
        while brower.current_url ==  "https://jp.shein.com/":
            ShCookies  = brower.get_cookies()
            brower.quit()
            with open('shein.json','w',encoding="utf-8") as f:
                cookies = json.dumps(ShCookies)
                f.write(cookies)
            f.close()
            return cookies
# 加载获取的Cookies登录网站
def readSheinCookies():
    # if hava cookies file ,use it 
    # if not , getTaobaoCookies()
    if os.path.exists('shein.json'):
        with open('shein.json','r',encoding='utf-8') as f:
            listCookies=json.loads(f.read())
        cookie = [item["name"] + "=" + item["value"] for item in listCookies]
        ShCookies = '; '.join(item for item in cookie)
    else:
        ShCookies = getSheinCookies()
    return ShCookies
Shcookies = readSheinCookies()
ic(Shcookies)

url = "https://jp.shein.com/Honeyspot-Contrast-Stripe-Trim-Tartan-Oversized-Sweater-p-5023702-cat-1734.html"

headers={
    'cookie':Shcookies,
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

html=requests.get(url=url,headers=headers)



