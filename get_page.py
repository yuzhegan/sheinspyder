# encoding='utf-8

# @Time: 2021-12-25
# @File: %
#!/usr/bin/env
from icecream import ic
import requests
from bs4 import BeautifulSoup
import csv

url = "https://jp.shein.com/Women-Knitwear-c-2216.html?ici=CCCSN%3DWomenHomePage_ON%3DBanner_OI%3D1_CN%3Dcategory_TI%3D50001_aod%3D0_PS%3DHZ-6-1_ABT%3D0&scici=WomenHomePage~~ON_Banner%2CCN_category%2CHZ_Knitwear%2CHI_hotZoneuadal3wddc8~~6_1~~real_2216~~~~&srctype=homepage&userpath=%3EWomenHomePage%3EWomen-Knitwear&page="

def get_urls(url):
    datas = []
    for i in range(1,3):
        links = url + str(i)
        res = requests.get(links)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, "html.parser")
        # ic(soup.prettify)
        pieces = soup.find_all("section", {"class":"S-product-item j-expose__product-item product-list__item"})
        for piece in pieces:
            pies = piece.find("div",{"class":"S-product-item__name"})
            # ic(link)
            data_title = pies.text.strip()
            # ic(data_title)
            link = "https://jp.shein.com/" + str(pies.find("a").get("href"))
            data = [data_title, link]
            datas.append(data)
    return datas
def writ2csv(datas, path):
    with open (path, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["data-title", "href"])
        for data in datas:
            writer.writerow(data)
    f.close()

ic(len(get_urls(url)))
writ2csv(get_urls(url), "test.csv")



