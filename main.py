# encoding='utf-8

# @Time: 2021-12-28
# @File: %
#!/usr/bin/env
from icecream import ic
from get_page import *
from get_detail import *
from Change_language import *
import multiprocessing as mp
import time
index_url = "https://jp.shein.com/Women-Knitwear-c-2216.html?ici=CCCSN%3DWomenHomePage_ON%3DBanner_OI%3D1_CN%3Dcategory_TI%3D50001_aod%3D0_PS%3DHZ-6-1_ABT%3D0&scici=WomenHomePage~~ON_Banner%2CCN_category%2CHZ_Knitwear%2CHI_hotZoneuadal3wddc8~~6_1~~real_2216~~~~&srctype=homepage&userpath=%3EWomenHomePage%3EWomen-Knitwear&page="
# urls = get_urls(index_url)
urls = ["https://jp.shein.com/Drop-Shoulder-Solid-Sweater-p-5578237-cat-1734.html?scici=WomenHomePage~~ON_Banner,CN_category,HZ_Knitwear,HI_hotZoneuadal3wddc8~~6_1~~real_2216~~~~"]
path = "/home/dav/Downloads/chromedriver"
brower = webdriver.Chrome(executable_path=path)
brower.implicitly_wait(1)
brower.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """

})
datas = []

for i in range(len(urls)):
    # url = urls[i][1]
    url = urls[i]
    ic(url)
    try:
        if i == 0:
            change_Janpn = Change_language()
            change_Janpn.load(brower, url)
            # time.sleep(3)
            data = Get_Deatil_Info(brower, url)
            datas += data
        else:
            brower.get(url)
            # time.sleep(3)
            data = Get_Deatil_Info(brower, url)
            datas += data
    except Exception as e: 
        Writ2Csv(datas)
# ic(datas)
Writ2Csv(datas)
