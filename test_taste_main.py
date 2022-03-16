from array import array
from turtle import onclick
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import re


def main():
    array_article_text = ['首頁', '\r\n                                買東西阿                            ', '\r\n                                美食                            ', '\r\n                                品飲                            ', '\r\n                                旅行                            ', '\r\n                                熱門                            ', '\r\n                                懶人包                            ', '\r\n                                節目                            ', '\r\n                                店家                            ', '\r\n                                1﹒   2                            ', '\r\n                                123                            ', '\r\n                                good                            ']
    # my_list = ['南機場夜市別只晚上去！５家早市必訪小吃：米其林推薦臭豆腐、老字號焢肉飯']
    resp = requests.get("https://supertaste-pre.tvbs.com.tw/")
    soup = BeautifulSoup(resp.text, 'html.parser')

    div = soup.find('div', class_='header_menu_nav')
    article_List = []
    for div_article in div.find_all(href=True):
        article_List.append(div_article.text)
    print(article_List)

    article_name = "品飲"
    str_match = [s for s in array_article_text if s.__contains__(article_name)]
    print(str_match)
    if(str_match):
        print("1")
        print(article_name)
    else:
        print("0")




if __name__ == '__main__':
    # -*- coding: UTF-8 -*-
    main()

