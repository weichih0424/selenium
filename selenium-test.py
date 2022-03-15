from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

####登入帳號密碼
def login_old_backstage():
    search_input = browser.find_element_by_name("login_adm_name").send_keys('dev001')
    search_input = browser.find_element_by_name("login_adm_pw").send_keys('dev001dev001dev001')
    # search_input.send_keys(Keys.ENTER)    ###可使用
    browser.find_element_by_xpath(u"//input[@value='登入']").click()
    WebDriverWait(browser, 10)

####選擇要進入的功能管理
def choose_function_management():
    browser.find_element_by_xpath('//*[@id="tree"]/li[19]/span').click()    ###食尚玩家
    # browser.get("http://2017back-pre.tvbs.com.tw/index.php/admission_list/left")
    browser.find_element_by_xpath('//*[@id="tree"]/li[19]/ul/li[5]/a').click()     ###文章總覽-網站編輯
    # browser.find_element_by_link_text("文章總覽-網站編輯").click()        ###無法使用
    # WebDriverWait(browser, 30)
    time.sleep(2)

####設定查詢條件
def Ssearch_Conditions():
    search_input = browser.find_element_by_name("search_keyword").send_keys('123')     ##關鍵字
    search_input = browser.find_element_by_name("search_articles_id").send_keys('123')       ##文章ID
    browser.find_element_by_xpath(u"//input[@value='查詢']").click()      ##查詢

###新增文章
def article_create():
    search_url()
    classification()
    post_time(time_now)
    # title()
###網址
def search_url():
    search_input = browser.find_element_by_name("search_url").send_keys('123')
###分類
def classification():
    search_input = browser.find_element_by_xpath('//*[@id="categories"]/div/div[1]/input')
    search_input.send_keys('52')
    search_input.send_keys(Keys.ENTER)

###發布時間
def post_time(time_now):
    search_input = browser.find_element_by_name("publish")
    search_input.clear()
    search_input.send_keys(time_now)

###文章標題
def title():
    search_input = browser.find_element_by_xpath('//*[@id="title"]')
    search_input.clear()
    search_input.send_keys('52')
# 指定存取網址
url="http://2017back-pre.tvbs.com.tw/index.php/login"

# 指定WebDriver路徑
# 要用變數指定chromedriver的放置路徑
chromedriver_path = '/usr/local/bin/chromedriver' 
browser=webdriver.Chrome(chromedriver_path)
browser.get(url)

time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# # 設定指令：在Google搜尋框中自動填入搜尋關鍵字，並搜尋。
# search_input = browser.find_element_by_name("q")
# search_input.send_keys('TechMarks Python Selenium')
# start_search_btn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "btnK")))
# start_search_btn.click()
try:
    login_old_backstage()
    browser.switch_to.frame("leftFrame")
    choose_function_management()
    # browser.switch_to.parent_frame()      ###可使用
    browser.switch_to.default_content()
    browser.switch_to.frame("mainFrame")
    ##等待新增按鈕加載完成
    btn_create = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-list_table"]/table/tbody/tr[1]/th/a/input')))
    ##點選新增按鈕
    btn_create.click()
    # Ssearch_Conditions()
    ##點選編輯按鈕
    # browser.find_element_by_xpath('//*[@id="content-list_table"]/table/tbody/tr[3]/td[9]/a/img').click()
    ##點選新增按鈕
    # browser.find_element_by_xpath('//*[@id="content-list_table"]/table/tbody/tr[1]/th/a/input').click()
    
    time.sleep(2)
    article_create()
    time.sleep(2)
except:
    # 錯誤顯示
    print("NO")
finally:
    # 關閉此次執行的WebDriver
    browser.close()
    