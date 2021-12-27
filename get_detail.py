# encoding='utf-8

# @Time: 2021-12-25
# @File: %
#!/usr/bin/env
from icecream import ic
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import json
import time
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
url = "https://jp.shein.com/Honeyspot-Solid-Fluffy-Sweater-p-7416907-cat-1734.html?scici=WomenHomePage~~ON_Banner,CN_category,HZ_Knitwear,HI_hotZoneuadal3wddc8~~6_1~~real_2216~~~~"


path = "/home/dav/Downloads/chromedriver" 
# %%
# 关闭弹窗 模拟登录, 登录之后没有弹窗

brower = webdriver.Chrome(executable_path=path)
# 手动登录获取Sheincookies
# 加载获取的Cookies登录网站

# %%
# def Get_DetilPage(url):
# 通过网页地址打开网页，此时会弹出浏览器，并加载相应的网页
brower.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """

})
brower.get(url)
time.sleep(2)

# 等待弹窗, 点击关闭按钮
try:
    WebDriverWait(brower, 10).until(EC.presence_of_element_located(
      (By.CLASS_NAME, "c-coupon-box")))
    brower.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/i").click()
    time.sleep(3)
except Exception as e:
    print(e)

# 切换语言为日语 点击语言列表
try:
    # WebDriverWait(brower,10).until(EC.presence_of_element_located(
        # (By.CLASS_NAME, "iconfont-critical icon-head-global")))
    brower.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[5]/a/span/i").click()
    time.sleep(5)

except Exception as e:
    print(e)
# 切换语言为日语

try:
    # WebDriverWait(brower, 10).until(EC.presence_of_element_located(
      # (By.CLASS_NAME, "col-xs-4 j-change-language")))
    brower.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[5]/div/div[4]/a[2]").click()
    time.sleep(5)
except Exception as e:
    print(e)



# 这里不需要往下拉加载
# js="var q=document.documentElement.scrollTop=10000"  # 滚动到最下面
# brower.execute_script(js)
#######      shein 是已颜色为一个SKU的, 颜色下面分尺码, sku1-s, sku2-s
soup = BeautifulSoup(brower.page_source, "lxml")
# %%
def Get_sku(soup):
    sku_doc = soup.find("div", {"class":"product-intro__head-sku-ctn"})
    sku = sku_doc.text.strip()
    # 'SKU: sw2109223427331015 (3051 Reviews)'
    sku = sku.split("(")[0][5:].strip()
    ic(sku)
    return sku
# ic(Get_sku(soup))

# %%
#pirce
def Get_price(soup):
    price_doc = soup.find("div", {"class":"original"})
    price = price_doc.text.strip()
    ic(price)
    return price
# ic(Get_price(soup))


# %%
# brand
def Get_brand(soup):
    brand_doc = soup.find("div", {"class":"product-intro__brand-name"})
    brand = brand_doc.text.strip()
    return brand
    # ic(brand)
# %%
# 重构title 品牌都大些情况, DAZY 标题 Dazy-Less
def Get_new_title(soup,brand):
    title_doc = soup.find("div", {"class":"product-intro__head-name"})
    title_n  = title_doc.text.strip()
    # 因为日文转换大些不影响,所有可以标题都转换大些
    title = title_n.upper().replace(brand.upper(), "").strip()
    return title
    # ic(title)


# %%
# colors Shein颜色名称是可以重复的,亚马逊上不允许,这里就处理掉了,重复的话, 后面加abcd
# 如果输出colors = [] 则表示这个链接只有一个颜色
def Get_colors_not_duplict(soup):
    color2 = ""
    list_color = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    colors_toc = soup.find_all("div", {"class":"product-intro__color-radio"})
    colors = []
    for item in colors_toc:
        color = item.get("aria-label").strip()
        if color not in colors:
            colors.append(color)
        else:
            for i in range(8):
                color2 = color + list_color[i]
                if color2 not in colors:
                    break
            colors.append(color2)
    return colors
    # ic(colors)
# %%
# 获取尺码名称
def Get_size_name(soup):
    size_doc = soup.find_all("div", {"class": "product-intro__size-radio-inner"})
    sizes = []
    for item in size_doc:
        sizes.append(item.text.strip())
    return sizes
    # ic(sizes)

# %%
# 获取描述,详情
def Get_desc(soup):
    desc_docs = soup.find_all("div", {"class":"product-intro__description-table-item"})
    descs = []
    for doc in desc_docs:
        key = doc.find("div", {"class":"key"}).text.strip(":").strip()
        value = doc.find("div", {"class":"val"}).text.strip()
        data = {"key":key, "value":value} 
        descs.append(data)
    return descs
    # ic(descs)
    # ic(descs[0]["key"])


# %%
#  转字符串存储, "|"分割表示
def Get_Desc_str(descs):
    str_descs = ""
    for item in descs:
        priex = str(item) + "|"
        str_descs +=  priex
    str_descs = str_descs.strip("|") #最后那个|要删除
    return str_descs
    # ic(str_descs)

# %%
# 字符串转字典格式
def Get_Desc_dict(str_descs):
    dect_list = str_descs.split("|")
    dect_list = [eval(item) for item in dect_list]
    # ic(dect_list)
    # ic(dect_list[0]["key"])
    return dect_list


# %%
# 转换成描述内容 字符串格式 亚马逊描述的html格式
def Get_Amz_desc(descs):
    Str_desc = ""
    for desc in descs:
        str_dec = "<b>" + desc["key"] + ":</b>" + "&nbsp;&nbsp;&nbsp;" + desc["value"] + "</br>"
        Str_desc += str_dec
    # ic(Str_desc)
    return Str_desc


def add_space(n):
    string =""
    for i in range(n+6):   #日文字符和英文数字占位大小不一样 测试+4比较合理
        string += "&nbsp;"
    return string

# %%
# 获取尺码表
# DONE: 获取尺码表  <26-12-21, yuzhe> #
def Get_Size_Chart(soup):
    size_chart_doc = soup.find("table", {"class":"sg-table-base j-cm-table"})
    results = size_chart_doc.find_all("tr")
    rows = []
    for result in results:
        datas = result.find_all("td")
        row_datas  = []
        for data in datas:
            row_datas.append(data.text.strip())
        rows.append(row_datas)

    # ic(rows)
    # %%
    # 放在亚马逊描述中,做成html表格形式 亚马逊不支持table标签
    # &nbsp; 表示不换行空格
    tables = ""
    # for row_tr in rows:
        # for data in row_tr:
            # td_html =  data + "&nbsp;"
            # tables += td_html
        # tables += "</br>"
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if i == 0: 
                td_html = rows[i][j] + "&nbsp;&nbsp;&nbsp;"
                tables += td_html
            else: 
                need_space = len(rows[0][j]) - len(rows[i][j])
                spaces = add_space(need_space)
                td_html = rows[i][j] + "&nbsp;" + spaces
                tables += td_html
        tables += "</br>"
    return tables
    # ic(tables)

# %%
def Get_Amz_Description(tables, Str_desc):
    description = tables + "</br></br>" + Str_desc
    return description

# %%
#image other -- can find the main image
# color1 的图片
def Get_color_image(soup):
    other_image_docs = soup.find_all("div",{"class":"product-intro__thumbs-item"})
    other_images = []
    for doc in other_image_docs:
        image = "https:" + doc.img.get("src")
        big_image = image.split("_thumb")[0] + ".jpg"
        other_images.append(big_image)
    # ic(other_images)
    return other_images
# ic(Get_color_image(soup))
# %%
elements = brower.find_elements_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div")
for i in range(1, len(elements)):
    elements[i].click()
    time.sleep(10)
    # js重新加载网页,网页内容会变化,如果还用之前的soup数据不会变化
    soups = BeautifulSoup(brower.page_source, "lxml")
    ic(Get_color_image(soups))
    ic(Get_sku(soups))

# %%
# TODO: 重构数据  <26-12-21, yuzhe> #
# 以颜色为一个sku, sku-s sku-m 这种格式, 父产品随机选一个, 读入每个颜色的数据,有多少颜色就需要做上一步多少次 不同的有"价格" "图片链接", 其他基本读一个就行, 尺码需要衍生出来, 读取尺码有多少个,颜色有多少个,衍生多少sku

