from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

from login import log_in
# import login

class back_end():
    
    def __init__(self):
        # chromedriver_path = '/usr/local/bin/chromedriver' 
        # browser = webdriver.Chrome(chromedriver_path)
        self.time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    ####關閉測試網站
    def close(self):
        browser.close()

    ####登入帳號密碼
    # def login_old_backstage(self):
    #     browser.get("http://2017back-pre.tvbs.com.tw/index.php/login")
    #     browser.find_element_by_name("login_adm_name").send_keys('dev001')
    #     browser.find_element_by_name("login_adm_pw").send_keys('dev001dev001dev001')
    #     # search_input.send_keys(Keys.ENTER)    ###可使用
    #     browser.find_element_by_xpath(u"//input[@value='登入']").click()
    
    ####選擇要進入的功能管理
    def choose_function_management(self):
        browser.switch_to.frame("leftFrame")
        # browser.find_element_by_xpath('//*[@id="tree"]/li[19]/span').click()    ###食尚玩家
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tree"]/li[19]/span'))).click()
        time.sleep(1)
        # browser.find_element_by_xpath('//*[@id="tree"]/li[19]/ul/li[5]/a').click()     ###文章總覽-網站編輯
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tree"]/li[19]/ul/li[5]/a'))).click()
        browser.switch_to.default_content()
        browser.switch_to.frame("mainFrame")

    ####選擇新增按鈕
    def to_article_create(self):
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-list_table"]/table/tbody/tr[1]/th/a/input'))).click()
        self.search_url()
        self.classification()
        self.post_time()
        self.title()
        self.player()
        self.author()
        self.cover_image()
        self.content()
        self.tag()
        self.status()

    ####網址
    def search_url(self):
        browser.find_element_by_name("search_url").send_keys('123')

    ####分類
    def classification(self):
        search_input = browser.find_element_by_xpath('//*[@id="categories"]/div/div[1]/input')
        search_input.send_keys('52')
        search_input.send_keys(Keys.ENTER)

    ####發布時間
    def post_time(self):
        search_input = browser.find_element_by_name("publish")
        search_input.clear()
        search_input.send_keys(self.time_now)

    ####文章、社群、SEO標題
    def title(self):
        search_input = browser.find_element_by_name("title")
        search_input.send_keys('test'+time.strftime(' %H:%M:%S', time.localtime()))
        search_input = browser.find_element_by_name("og_title").click()
        search_input = browser.find_element_by_name("seo_title").click()

    ####玩家
    def player(self):
        Select(browser.find_element_by_name('player_kind')).select_by_visible_text(u"部落客")
        Select(browser.find_element_by_name('player_id'))
        search_input = browser.find_element_by_class_name('searchable-select-holder').click()
        search_input = browser.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input')
        search_input.send_keys('GA 測試')
        search_input.send_keys(Keys.ENTER)

    ####上搞者名稱
    def author(self):
        Select(browser.find_element_by_name('author')).select_by_index(1)

    ####主圖URL、社群分享圖URL
    def cover_image(self):
        browser.find_element_by_name("cover_image").send_keys('/program_piwigo/piwigo/_data/i/upload/2022/03/03/20220303152956-f1ae3e16-xs.jpg')
        browser.find_element_by_name("ogimage").click()

    ####內容
    def content(self):
        text = "1\n2\n3\n4\n5\n6"

        browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe'))
        if "\n" in text: #check if exists \n tag in text
            textarea = browser.find_element_by_id('article_content')
            textsplit = text.split("\r\n") #explode
            textsplit_len = len(textsplit)-1 #get last element
            for text in textsplit:
                textarea.send_keys(text)
                if textsplit.index(text) != textsplit_len: #do what you need each time, if not the last element
                    textarea.send_keys(Keys.SHIFT+Keys.ENTER)
        else:
            browser.find_element_by_id('article_content').send_keys('52')
        browser.switch_to.default_content()
        browser.switch_to.frame("mainFrame")

    ####TAG
    def tag(self):
        search_input = browser.find_element_by_xpath('//*[@id="tag_row"]/td[2]/div[1]/div[1]/input')
        search_input.send_keys('12')
        search_input.send_keys(Keys.ENTER)

    ####發布狀態
    def status(self):
        Select(browser.find_element_by_name('status')).select_by_value("1")

    ####儲存
    def title_save(self):
        browser.find_element_by_id("submitBtn").click()

    ####彈跳視窗
    def alert(self):
        alert = browser.switch_to.alert
        alert.accept() #接受現有警告框，相當於確認
        time.sleep(1)
        alert.accept()


if __name__=="__main__":
    chromedriver_path = '/usr/local/bin/chromedriver' 
    browser = webdriver.Chrome(chromedriver_path)

    try:
        backend = back_end()
        login = log_in()
        login.login_old_backstage(browser)
        # backend.login_old_backstage()
        backend.choose_function_management()
        backend.to_article_create()
        # backend.title_save()
        # backend.alert()
        time.sleep(5)
    except:
        # 錯誤顯示
        print("NO")
    finally:
        # 關閉此次執行的WebDriver
        backend.close()