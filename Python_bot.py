from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time,random

class Bot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        bot = self.bot
        bot.get("http://www.instagram.com")
        time.sleep(5)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        bot.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]").click()
        time.sleep(10)
        bot.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        

    # element here refers to the follwer name
    def profile(self,element):
        self.bot.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
        time.sleep(5)
        self.bot.find_element_by_partial_link_text('followers').click()
        time.sleep(5)
        scroll_box=self.bot.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht,ht=0,1
        while last_ht!=ht:
            last_ht=ht
            time.sleep(1)
            ht=self.bot.execute_script("""
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """,scroll_box)
        links=scroll_box.find_elements_by_tag_name('a')
        for name in links:
            if element in name.text:
                name.click()
                break
           
        
    def firstpic(self):
        self.bot.find_element_by_class_name("_9AhH0").click()
        time.sleep(3)

    def next_pic(self):
        time.sleep(2)
        next=self.bot.find_element_by_partial_link_text('Next')
        time.sleep(1)
        return next

    def like_pic(self):
        if self.bot.find_elements_by_css_selector("[aria-label='Unlike']"):
            print("Already Liked")
        else:
            print("Liked now")
            self.bot.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
        
    def comment(self):
        my_bot.bot.find_element_by_css_selector("[aria-label='Comment']").click()
        time.sleep(1)
        a=['Nicepic !!!','You’re classy','stunning','You are graceful']
        q=random.choice(a)
        my_bot.bot.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea").send_keys(q)
        time.sleep(1)
        self.bot.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button").click()
        time.sleep(15)  
            
           
    def continue_Liking(self):
        while(True):
            nex=self.next_pic()
            if nex!=False:
                nex.click()
                time.sleep(2)
                self.like_pic()
                time.sleep(2)
                self.comment()
                time.sleep(30)
            else:
                print("Not Found")
                break

#username=Useraname of instagram
#password=password
my_bot = Bot("username", "password")

