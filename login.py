from selenium import webdriver
import time

class log_in():
    def __init__(self):
        pass

    ####登入帳號密碼
    def login_old_backstage(self,browser):
        browser.get("http://2017back-pre.tvbs.com.tw/index.php/login")
        browser.find_element_by_name("login_adm_name").send_keys('dev001')
        browser.find_element_by_name("login_adm_pw").send_keys('dev001dev001dev001')
        # search_input.send_keys(Keys.ENTER)    ###可使用
        browser.find_element_by_xpath(u"//input[@value='登入']").click()


if __name__=="__main__":
    chromedriver_path = '/usr/local/bin/chromedriver' 
    browser = webdriver.Chrome(chromedriver_path)

    login = log_in()
    login.login_old_backstage(browser)
    time.sleep(3)
    browser.close()