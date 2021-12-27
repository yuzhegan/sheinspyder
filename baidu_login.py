# encoding='utf-8

# @Time: 2021-12-25
# @File: %
#!/usr/bin/env
from icecream import ic
import time
from selenium import webdriver
import json
import os

brower = webdriver.Chrome(executable_path="/home/dav/Downloads/chromedriver")
login_url = "https://passport.baidu.com/v2/?reg&tt=1640490780118&overseas=undefined&gid=52E5BCE-FFC7-4A57-BEF2-4D29153CF5E7&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2F"
def getSheinCookies():
    # get login taobao cookies
    brower.get(login_url)
    while True:
        print("Please login in shein.com!")
        time.sleep(3)
        # if login in successfully, url  jump to www.taobao.com
        while brower.current_url ==  "https://www.baidu.com/":
            ShCookies  = brower.get_cookies()
            brower.quit()
            with open('baidu.txt','w',encoding="utf-8") as f:
                cookies = json.dumps(ShCookies)
                f.write(cookies)
            f.close()
            return cookies
# 加载获取的Cookies登录网站
def readSheinCookies():
    # if hava cookies file ,use it 
    # if not , getTaobaoCookies()
    if os.path.exists('baidu.txt'):
        readPath = open('baidu.txt','r')
        ShCookies = json.load(readPath)
    else:
        ShCookies = getSheinCookies()
    return ShCookies
Shcookies = readSheinCookies()

brower.get("https://www.baidu.com")

for cookie in Shcookies:
    if "expiry" in cookie:
        del cookie["expiry"]
    brower.add_cookie(cookie)
time.sleep(5)

brower.refresh()

time.sleep(10)
