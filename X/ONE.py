from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class to_target_function():
    def __init__(self,target_func):
        self.target_func =target_func 
        # chromedriver_path = '/usr/local/bin/chromedriver' 
        # self.browser=webdriver.Chrome(chromedriver_path)
        self.driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
        # self.driver = webdriver.Chrome(executable_path=r'D:\drivers\chromedriver.exe')
        self.txt_1 = '我做的義式水煮魚跟烤紙包菜菜真是太好吃了，希望你們知道\n'+ '我做的義式水煮魚跟烤紙包菜菜真是太好吃了，希望你們知道\n'
        self.txt_2 = '我做的義式水煮魚跟烤紙包菜菜真是太好吃了，希望你們知道\n''我做的義式水煮魚跟烤紙包菜菜真是太好吃了，希望你們知道'
        self.frametxt = '<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fhanhanpovideo%2Fposts%2F486813323003338&show_text=true&width=500" width="500" height="632" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
    def enter_back(self):
        self.driver.get("http://2017back-st.tvbs.com.tw/index.php/login")
        self.driver.find_element_by_id("login_adm_name").send_keys("dev001")
        self.driver.find_element_by_id("login_adm_pw").send_keys("dev001dev001dev001")
        self.driver.find_element_by_xpath('//*[@id="change-form"]/table/tbody/tr[3]/td/input').click()
        time.sleep(2) 
        
    def add_news(self,test_link):
        self.driver.get("http://2017back-st.tvbs.com.tw/index.php/news_management/news_a/news_add/master")
        self.driver.find_element_by_class_name("news_title").send_keys("hahabimo")  #長標
        self.driver.find_element_by_class_name("short_title").send_keys("hahabimo") #短標
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/table/tbody/tr[7]/td[2]/input[1]').click() #分類
        self.driver.find_element_by_name("news_summary").send_keys("hahabimo") #導言
        self.driver.find_element_by_name("news_img").send_keys("https://cc.tvbs.com.tw/img/upload/2022/02/28/20220228103543-42a7ceb5.jpg") #主圖
        self.driver.find_element_by_xpath('//*[@id="content-list_table"]/form/table/tbody/tr[19]/td[2]/div[1]/div[1]/input').send_keys("hahabimo") #標籤
        self.driver.find_element_by_xpath('//*[@id="content-list_table"]/form/table/tbody/tr[19]/td[2]/div[1]/div[1]/input').send_keys(Keys.ENTER)


        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe'))
        self.driver.find_element_by_tag_name('body').send_keys(self.txt_1)
        self.driver.switch_to.default_content()

        self.driver.find_element_by_xpath('//*[@id="embed_article"]').send_keys(self.frametxt)
        self.driver.find_element_by_xpath('//*[@id="embed_btn"]').click()

        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe'))
        self.driver.find_element_by_tag_name('body').send_keys(self.txt_2)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('//*[@id="content-list_table"]/form/table/tbody/tr[22]/td[1]/input[3]').click()

        
        time.sleep(5)
        # self.driver.quit()

test_1 = to_target_function("http://2017back-st.tvbs.com.tw/index.php/news_management/news_a/news_list/master/news")
test_1.enter_back()
test_1.add_news('<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fupfdream%2Fposts%2F753197899422826&show_text=true&width=500" width="500" height="674" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>')
