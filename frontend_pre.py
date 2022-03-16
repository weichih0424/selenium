from array import array
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time


class supertaste_pre():
    def __init__(self):
        self.taste = "https://supertaste-pre.tvbs.com.tw/"
        self.health = "https://health-pre.tvbs.com.tw/"
        self.woman = "https://woman-pre.tvbs.com.tw/"
        
    
    ####選擇三網登入，回傳“網址”、“分類class”、“文章class”、“文章class的text”
    def login_old_backstage(self,browser,url):
        if(url == "食尚"):
            url_frontend = self.taste
            which_class = 'header_menu_nav'
            article_class_name = 'talk_article'
            article_class_name_text = 'txt'
            browser.get(url_frontend)
            return url_frontend, which_class, article_class_name, article_class_name_text
        elif(url == "健康"):
            url_frontend = self.health
            which_class = 'menu_bar'
            article_class_name = 'center category_center'
            article_class_name_text = 'title'
            browser.get(url_frontend)
            return url_frontend, which_class, article_class_name, article_class_name_text
        elif(url == "女大"):
            url_frontend = self.woman
            which_class = 'menu'
            article_class_name = 'category_content_box'
            article_class_name_text = 'title a22'
            browser.get(url_frontend)
            return url_frontend, which_class, article_class_name, article_class_name_text
        else:
            supertaste_pre.login_old_backstage(browser,input("輸入網址："))
    ####傳入 “input分類名稱的值”、“網址”、“分類class”
    def search_box(self,search_box,url_login_frontend,which_login_class):
        resp = requests.get(url_login_frontend)
        # resp = requests.get(self.taste)                               ###食尚
        # resp = requests.get(self.health)                              ###健康
        # resp = requests.get(self.woman)                               ###女大
        soup = BeautifulSoup(resp.text, 'html.parser')
        div = soup.find('div', class_=which_login_class)
        # div = soup.find('div', class_='header_menu_nav')              ###食尚
        # div = soup.find('div', class_='menu_bar')                     ###健康
        # div = soup.find('div', class_='menu')                         ###女大

        article_List = []
        for div_article in div.find_all(href=True):
            article_List.append(div_article.text)
        print(article_List)
        if (search_box):
            print(search_box)
            browser.find_element_by_link_text(search_box).click()
        else:
            supertaste_pre.search_box(input("分類："))
        # browser.find_element_by_link_text(search_box).click() if (search_box in array_search_box) else supertaste_pre.search_box(input("分類："))
    
    ###傳入 “input搜尋文章名稱”、“文章class”、“文章class的text”
    def article_name(self,article_name,article_class_name,article_class_name_text):
        # -*- coding: UTF-8 -*-
        resp = requests.get(browser.current_url)
        # print (browser.current_url)
        # resp = requests.get("https://supertaste-pre.tvbs.com.tw/food")        ###食尚
        # resp = requests.get("https://health-pre.tvbs.com.tw/medical")         ###健康
        # resp = requests.get("https://woman-pre.tvbs.com.tw/fitness")          ###女大
        soup = BeautifulSoup(resp.text, 'html.parser')
        div = soup.find('div', class_=article_class_name)
        article_class_txt_s = div.find_all('div',class_=article_class_name_text)

        # div = soup.find('div', class_='talk_article')                         ###食尚
        # article_class_txt_s = div.find_all('div',class_='txt')

        # div = soup.find('div', class_='center category_center')               ###健康
        # article_class_txt_s = div.find_all('div',class_='title')

        # div = soup.find('div', class_='category_content_box')                 ###女大
        # article_class_txt_s = div.find_all('div',class_='title a22')

        array_article_text = []
        for article_class_txt in article_class_txt_s:
            array_article_text.append(article_class_txt.text)
        print(array_article_text)
        str_match = [s for s in array_article_text if s.__contains__(article_name)]
        str_match = str(str_match).encode('utf-8').decode('utf-8')
        if (str_match):
            print(str_match)
            browser.find_element_by_partial_link_text(article_name).send_keys(Keys.TAB)
            browser.find_element_by_partial_link_text(article_name).click()
        else:
            print("0")
            supertaste_pre.article_name(input("文章："))
        # browser.find_element_by_partial_link_text(article_name).send_keys(Keys.TAB),browser.find_element_by_partial_link_text(article_name).click() if (str_match) else supertaste_pre.article_name(input("文章："))
        

if __name__=="__main__":

    chromedriver_path = '/usr/local/bin/chromedriver' 
    browser = webdriver.Chrome(chromedriver_path)
    supertaste_pre = supertaste_pre()
    # supertaste_pre.login_old_backstage(browser,"https://woman-pre.tvbs.com.tw/")
    # supertaste_pre.search_box('瘦身') 
    # supertaste_pre.article_name('/html/body/div[11]/div[3]/div/div[6]/div[1]/div[2]/div[1]/div/li[1]')### <li data-articleid="20032">
    
    # supertaste_pre.login_old_backstage(browser,"https://health-pre.tvbs.com.tw/")
    # supertaste_pre.search_box('醫療')
    # supertaste_pre.article_name('//*[@id="combolistUl"]/li[1]/a/div[2]/div[1]')### <div class="title"> or <span>

    # supertaste_pre.login_old_backstage(browser,"https://supertaste-pre.tvbs.com.tw/")
    # supertaste_pre.search_box("美食")
    # supertaste_pre.article_name('//*[@id="combolistUl"]/ul[1]/li[1]/a/div[2]')

    url_login_frontend, which_login_class, article_class_name, article_class_name_text = supertaste_pre.login_old_backstage(browser,input("輸入網址："))
    supertaste_pre.search_box(input("分類："),url_login_frontend,which_login_class)
    supertaste_pre.article_name(input("文章："),article_class_name,article_class_name_text)

    time.sleep(3)
    browser.close()
    

