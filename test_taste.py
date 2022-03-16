from array import array
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time


# class supertaste_pre():
#     def __init__(self):
#         pass
    
#     ####登入帳號密碼
#     def login_old_backstage(self,browser):
#         html = browser.get("https://supertaste-pre.tvbs.com.tw/")
#     def search(self):
#         print(soup.find_all('ul'))
    
# if __name__=="__main__":
#     soup = BeautifulSoup(html, 'html.parser')
#     chromedriver_path = '/usr/local/bin/chromedriver' 
#     browser = webdriver.Chrome(chromedriver_path)
#     supertaste_pre = supertaste_pre()
#     supertaste_pre.login_old_backstage(browser)
#     supertaste_pre.search()

#     time.sleep(3)
#     browser.close()

def main():
    array_article_text = ['南機場夜市別只晚上去！５家早市必訪小吃：米其林推薦臭豆腐、老字號焢肉飯', '2022全台霸氣早餐17間！爆量三明治、蛋餅、飯糰統統有，起司控、肉控快筆記', '789', '456', '爆漿牽絲太狂！台南大東夜市５家必吃「邪惡美食」：爆滿玉米杯、牽絲起司棒']
    # my_list = ['南機場夜市別只晚上去！５家早市必訪小吃：米其林推薦臭豆腐、老字號焢肉飯']
    resp = requests.get("https://supertaste-pre.tvbs.com.tw/food")
    soup = BeautifulSoup(resp.text, 'html.parser')

    div = soup.find('div', id='combolistUl')
    div_article_name = div.find_all('div',class_='txt')
    article_List = []
    for div_article in div_article_name:
        article_List.append(div_article.text)
    # print(article_List)

    article_name = "南機場"

    # str_match = [s for s in array_article_text if article_name in s]
    str_match = [s for s in array_article_text if s.__contains__(article_name)]
    print(str_match)
    if(str_match):
        print("1")
        print(article_name)
    else:
        print("0")
        # str_match = [s for s in array_article_text if s.__contains__(article_name)]
        # if (str_match in array_article_text):
        #     browser.find_element_by_partial_link_text(article_name).send_keys(Keys.TAB)
        #     browser.find_element_by_partial_link_text(article_name).click()
        # else:
        #     supertaste_pre.article_name(input('文章：'))




if __name__ == '__main__':
    # -*- coding: UTF-8 -*-
    main()

