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
from Change_language import *
import csv
# url = "https://jp.shein.com/DAZY-Solid-Cable-Knit-Drop-Shoulder-Sweater-p-5835597-cat-1734.html?scici=WomenHomePage~~ON_Banner,CN_category,HZ_Knitwear,HI_hotZoneuadal3wddc8~~6_1~~real_2216~~~~"


# path = "/home/dav/Downloads/chromedriver" 
# # %%
# # 关闭弹窗 模拟登录, 登录之后没有弹窗

# brower = webdriver.Chrome(executable_path=path)
# # 手动登录获取Sheincookies
# # 加载获取的Cookies登录网站

# # %%
# # def Get_DetilPage(url):
# # 通过网页地址打开网页，此时会弹出浏览器，并加载相应的网页
# brower.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    # "source": """
    # Object.defineProperty(navigator, 'webdriver', {
      # get: () => undefined
    # })
  # """

# })
# brower.get(url)
# time.sleep(2)

# # 等待弹窗, 点击关闭按钮
# try:
    # WebDriverWait(brower, 10).until(EC.presence_of_element_located(
      # (By.CLASS_NAME, "c-coupon-box")))
    # brower.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/i").click()
    # time.sleep(3)
# except Exception as e:
    # print(e)

# # 切换语言为日语 点击语言列表
# try:
    # # WebDriverWait(brower,10).until(EC.presence_of_element_located(
        # # (By.CLASS_NAME, "iconfont-critical icon-head-global")))
    # brower.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[5]/a/span/i").click()
    # time.sleep(5)

# except Exception as e:
    # print(e)
# # 切换语言为日语

# try:
    # # WebDriverWait(brower, 10).until(EC.presence_of_element_located(
      # # (By.CLASS_NAME, "col-xs-4 j-change-language")))
    # brower.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[5]/div/div[4]/a[2]").click()
    # time.sleep(5)
# except Exception as e:
    # print(e)



# 这里不需要往下拉加载
# js="var q=document.documentElement.scrollTop=10000"  # 滚动到最下面
# brower.execute_script(js)
#######      shein 是已颜色为一个SKU的, 颜色下面分尺码, sku1-s, sku2-s


# %%
def Get_sku(soup):
    try:
        sku_doc = soup.find("div", {"class":"product-intro__head-sku-ctn"})
        sku = sku_doc.text.strip()
        # 'SKU: sw2109223427331015 (3051 Reviews)'
        sku = sku.split("(")[0][5:].strip()
    except Exception as e:
        sku = ""
    return sku

# %%
#pirce
def Get_price(soup):
    try:
        price_doc = soup.find("div", {"class":"original"}) #原价
        price = price_doc.text.strip()
    except Exception as e:
        try:
            price_doc = soup.find("del", {"class":"del-price"}) #打折价格, 取打折之前价格
            price = price_doc.text.strip()
        except Exception as e: 
            price =""
    return price


# %%
# brand
def Get_brand(soup):
    try:
        brand_doc = soup.find("div", {"class":"product-intro__brand-name"})
        brand = brand_doc.text.strip()
    except Exception as e: 
        brand = ""
    return brand
# %%
# 重构title 品牌都大些情况, DAZY 标题 Dazy-Less
def Get_new_title(soup,brand):
    try:
        title_doc = soup.find("h1", {"class":"product-intro__head-name"})
        title_n  = title_doc.text.strip()
        # 因为日文转换大些不影响,所有可以标题都转换大些
        title = title_n.upper().replace(brand.upper(), "").strip() #第三方有品牌的
        title = title_n.upper().replace("shein".upper(), "").strip() #shein自营的
    except Exception as e:
        title = ""
    return title


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
# %%
# 获取尺码名称
def Get_size_name(soup):
    size_doc = soup.find_all("div", {"class": "product-intro__size-radio-inner"})
    sizes = []
    for item in size_doc:
        sizes.append(item.text.strip())
    return sizes

# %%
# 获取描述,详情
#  详情用作字典来写入bullet_point , 返回列表来写入description 给两个返回值
def Get_desc(soup):
    desc_docs = soup.find_all("div", {"class":"product-intro__description-table-item"})
    descs = []
    dic_desc = {}
    for doc in desc_docs:
        key = doc.find("div", {"class":"key"}).text.strip(":").strip()
        value = doc.find("div", {"class":"val"}).text.strip()
        data = {"key": key, "value": value} #存入字典
        descs.append(data)
        dic_desc = {**{key:value}, **dic_desc}
    return [descs, dic_desc]

# %%
# 字典转字符串 descs为字典 
def Get_Desc_str(descs):
    str_descs = str(descs)
    # str_descs = ""
    # for item in descs:
        # priex = str(item) + "|"
        # str_descs +=  priex
    # str_descs = str_descs.strip("|") #最后那个|要删除
    return str_descs

# %%
# 字符串转字典格式
def Get_Desc_dict(str_descs):
    dect_list = str_descs.split("|")
    dect_list = [eval(item) for item in dect_list]
    return dect_list

# %%
# 转换成描述内容 字符串格式 亚马逊描述的html格式
def Get_Amz_desc(descs):
    Str_desc = ""
    for desc in descs:
        str_dec = "<b>" + desc["key"] + ":</b>" + "&nbsp;&nbsp;&nbsp;" + desc["value"] + "</br>"
        Str_desc += str_dec
    return Str_desc



def add_space(n):
    string =""
    for i in range(n+3):   #日文字符和英文数字占位大小不一样 测试+4比较合理
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
                td_html = rows[i][j] + "&nbsp;"
                tables += td_html
            else: 
                need_space = len(rows[0][j]) - len(rows[i][j])
                spaces = add_space(need_space)
                td_html = rows[i][j] + "&nbsp;" + spaces
                tables += td_html
        tables += "</br>"
    return tables
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
        doc = doc.find('img')
        if "src" in str(doc):
            try:
                image = "https:" + doc.get("src")
            except Exception as e:
                image = "https"  + doc.get("data-src")
            big_image = image.split("_thumb")[0] + ".jpg"
            other_images.append(big_image)
    return other_images
# %%
def Get_result_row(soup, color, url):
    sku = Get_sku(soup)
    brand = Get_brand(soup)
    price = Get_price(soup)
    new_title = Get_new_title(soup, brand)
    size_names = Get_size_name(soup)
    desc_list = Get_desc(soup)
    desc = desc_list[0]
    bullet_point = Get_Desc_str(desc_list[1])
    amz_desc = Get_Amz_desc(desc)
    size_chart = Get_Size_Chart(soup)
    description = Get_Amz_Description(size_chart, amz_desc)
    images_url = Get_color_image(soup)
    # 循环尺码,进行sku拼接, sku-s, sku-m
    def Get_image_link(n):
        n_image =""
        try:
            n_image = images_url[n]
        except Exception as e:
            n_image = ""
        return n_image
    shein_datas = []

    # 子产品
    for item in size_names:
        n_url = url
        n_size_name = item
        n_sku = sku + "-" + str(item)
        n_brand = brand
        n_price = price
        n_title = new_title + " " + color + " " + n_size_name #title add color & size
        n_bullet_point = bullet_point
        n_description = description
        n_image0 = Get_image_link(0)
        n_image1 = Get_image_link(1)
        n_image2 = Get_image_link(2)
        n_image3 = Get_image_link(3)
        n_image4 = Get_image_link(4)
        n_image5 = Get_image_link(5)
        n_image6 = Get_image_link(6)
        n_image7 = Get_image_link(7)
        data = [n_url, n_sku, n_brand, n_price, n_title, n_bullet_point, n_description, n_size_name, color, n_image0,n_image1, n_image2
                , n_image3,n_image4, n_image5, n_image6, n_image7]
        shein_datas.append(data)
    # ic(shein_datas)
    return shein_datas




# %%
def Get_Deatil_Info(brower, url):
    # url = "https://jp.shein.com/Drop-Shoulder-Eyelet-Detail-Sweater-p-4339026-cat-1734.html?scici=productDetail~~RecommendList~~RS_emarsys,RJ_NoFaultTolerant~~Customers%20Also%20Viewed~~SPcProductDetailCustomersAlsoViewedList~~0"
    # path = "/home/dav/Downloads/chromedriver" 
    # brower = webdriver.Chrome(executable_path=path)
    # 改变语言为日语
    # change_Janpn = Change_language()
    # change_Janpn.load(brower, url)
    datas = []
    list_color = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    colors = []  #存放颜色,防止一个listing颜色重复
    # 找到所有颜色
    elements = brower.find_elements_by_xpath("//div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]")
    for i in range(len(elements)):
        try:
            elements[i].click() #点击颜色
            time.sleep(3)
            # js重新加载网页,网页内容会变化,如果还用之前的soup数据不会变化
            soups = BeautifulSoup(brower.page_source, "lxml")
            color = soups.find("span", {"class" : "color-999"}).text.strip()
            if color not in colors: # 防止一个listing颜色重复, 重复则颜色后+a
                colors.append(color)
            else:
                for i in range(8):
                    color = color + list_color[i]
                    if color not in colors:
                        break
                colors.append(color)
            data = Get_result_row(soups,color, url)
            # datas.append(data)
            datas += data
        except Exception as e:   #只有单个颜色
            soup = BeautifulSoup(brower.page_source, "lxml")
            color = ""
            data = Get_result_row(soup, color, url)
            datas += data
    parent =[item for item in datas[0]]
    parent[1] = parent[1].split("-")[0]
    parent[3] = ""
    parent[7] = ""
    parent[8] = ""
    datas.insert(0,parent)
    return datas

# %%
def Writ2Csv(datas):
    with open("reslut.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["url","sku", "brand", "price", "title", "bullet_point", "description","size_name","color","image1", "image2", "image3", "image4", "image5", "image6", "image7", "image8"])
        for row in datas:
            writer.writerow(row)
    f.close()

# %%
# TODO: 重构数据  <26-12-21, yuzhe> #
# 以颜色为一个sku, sku-s sku-m 这种格式, 父产品随机选一个, 读入每个颜色的数据,有多少颜色就需要做上一步多少次 不同的有"价格" "图片链接", 其他基本读一个就行, 尺码需要衍生出来, 读取尺码有多少个,颜色有多少个,衍生多少sku

