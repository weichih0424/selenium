from array import array
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class supertaste_pre():
    def __init__(self):
        pass
    
    ####登入帳號密碼
    def login_old_backstage(self,browser,url):
        if(url == "食尚"):
            browser.get("https://supertaste-pre.tvbs.com.tw/")
        elif(url == "健康"):
            browser.get("https://health-pre.tvbs.com.tw/")
        elif(url == "女大"):
            browser.get("https://woman-pre.tvbs.com.tw/")
        else:
            supertaste_pre.login_old_backstage(browser,input("輸入網址："))
    
    def search_box(self,search_box):
        array_search_box = ["美食","醫療","瘦身"]
        if (search_box in array_search_box):
            browser.find_element_by_link_text(search_box).click()
        else:
            supertaste_pre.search_box(input("分類："))
    
    def article_name(self,article_name):
        array_article_name = ["南機場","你好","0929"]
        if (article_name in array_article_name):
            browser.find_element_by_partial_link_text(article_name).send_keys(Keys.TAB)
            browser.find_element_by_partial_link_text(article_name).click()
        else:
            supertaste_pre.article_name(input('文章：'))
        
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

    supertaste_pre.login_old_backstage(browser,input("輸入網址："))
    supertaste_pre.search_box(input("分類："))
    supertaste_pre.article_name(input("文章："))


    time.sleep(3)
    browser.close()
    

