from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
from random import randint
from dotenv import  load_dotenv
import os 
import pyautogui
import comments




def sleep_rand():
    sleep(randint(1,3))

        

class DirectMessagePage:
    def __init__(self,browser):
        self.browser = browser
        sleep_rand()

    def go_to_small_business(self):
        engagement_group = browser.find_element_by_xpath("//*[text()='Small Businesses']")
        engagement_group.click()
        sleep_rand()

    def load_messages(self, hold_time):
        group_chat_element = browser.find_element_by_xpath("//div[@class='JiVIq _0NM_B']")
        group_chat_element.click()
    
        import time 
        start = time.time();
        while time.time() - start <= hold_time:
            pyautogui.press('up')

    def __like_comment(self, profile_link):



        main_window = self.browser.current_window_handle
        profile_link.send_keys(Keys.CONTROL + Keys.RETURN)
        sleep_rand()
        self.browser.switch_to.window(browser.window_handles[1])
        sleep_rand()

        # Profile Page Coding
        first_picture = self.browser.find_element_by_xpath("//div[@class='eLAPa']")
        first_picture.click()
        
        # post = self.browser.find_element_by_xpath("//div[@class = '_2dDPU CkGkG']")  

        sleep_rand()
        exit_button = self.browser.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="svg"][@aria-label="Close"]')
        like_button = self.browser.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="svg"][@aria-label="Like"]')
        comment_textarea = self.browser.find_element_by_xpath('//textarea[@class="Ypffh"]')
       

        
        sleep_rand()
        print("liked photo")
        like_button.click()
        sleep_rand()

        print("clicked on textarea")
        comment_textarea.click()
        sleep(1)
        comment_textarea = self.browser.find_element_by_xpath('//textarea[@aria-label="Add a comment…"]')
        comment_textarea.send_keys(comments.get_random_comment())
        
        sleep_rand()
        comment_post = self.browser.find_element_by_xpath('//button[contains(@class, "sqdOP") and contains(@class, "yWX7d") and contains(@class, "y3zKF") and contains(@type, "submit")]')
        comment_post.click()
        print("comment posted")
        sleep_rand()

        exit_button.click()
 
        

        self.browser.close()
        self.browser.switch_to.window(browser.window_handles[0])



    def revert_messages(self, posts):
        # messages = browser.find_elements_by_xpath("//div[@class='Igw0E  Xf6Yq  eGOV_ ybXk5 _4EzTm']")
        messages = browser.find_elements_by_css_selector('div.Igw0E.Xf6Yq.eGOV_.ybXk5._4EzTm')[::-1]
        print(len(messages))
        count = 0
        for m in messages:
            if count == posts:
                break
            count += 1 

            try:
                sleep_rand()
                browser.execute_script("arguments[0].scrollIntoView(true)", m)
               
                like_message = m.find_element_by_xpath(".//span[@class='uTSKe']")
                profile = m.find_element_by_xpath(".//a[contains(@class, '_2dbep') and contains(@class, 'qNELH') and contains(@class, 'kIKUG')]")
                actions = ActionChains(self.browser)
                actions.double_click(like_message).perform()
                self.__like_comment(profile)
            except:
                 print(m.get_attribute('innerHTML'))
                 continue
            
            
    
            



class HomePage: 
    def __init__(self,browser):
        self.browser = browser
        sleep_rand()
        self.ignore_popups()

    def ignore_popups(self):
        
        save_info = self.browser.find_element_by_xpath("//button[@type='button' and contains(.,'Not Now')]")
        save_info.click()
        sleep_rand()
        notifications = self.browser.find_element_by_xpath("//button[@tabindex='0' and contains(.,'Not Now')]")
        notifications.click()
        sleep_rand()

    def go_to_direct_messages(self):
        dm_button = self.browser.find_element_by_xpath("//a[@href='/direct/inbox/']")
        dm_button.click()
        return DirectMessagePage(self.browser)

class LoginPage:

    def __init__(self,browser):
        self.browser = browser
        self.browser.implicitly_wait(randint(4,6))
        browser.get("https://instagram.com/")
    
    def login(self, username, password):
        username_input = self.browser.find_element_by_xpath("//input [@name='username']")
        password_input = self.browser.find_element_by_xpath("//input[@name='password']")
        login_button   = self.browser.find_element_by_xpath("//button[@type='submit']")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()  
        
        return HomePage(self.browser)




def main():

    load_dotenv()
    USERNAME = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")

    browser = webdriver.Firefox()
    sleep_rand()

    login_page = LoginPage(browser)
    home_page = login_page.login(USERNAME, PASSWORD)
    dm_page = home_page.go_to_direct_messages()
    dm_page.go_to_small_business()
    sleep(3)
    dm_page.load_messages(10)
    dm_page.revert_messages(30)


    print("Script has finished")



main()