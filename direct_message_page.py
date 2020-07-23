import constants
import pyautogui

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


class DirectMessagePage:
    def __init__(self,browser):
        self.browser = browser
        self.browser.implicitly_wait(constants.random_time())


        # self.browser.implicitly_wait(constants.random_time())

    def go_to_small_business(self):
        engagement_group = self.browser.find_element_by_xpath(constants.paths["engagement_group"])
        engagement_group.click()
        constants.sleep_rand()

    def load_messages(self, hold_time):
        group_chat_element = self.browser.find_element_by_xpath(constants.paths["group_chat_element"])
        group_chat_element.click()
    
        import time 
        start = time.time();
        while time.time() - start <= hold_time:
            pyautogui.press('up')

    def __like_comment(self, profile_link):



        main_window = self.browser.current_window_handle
        profile_link.send_keys(Keys.CONTROL + Keys.RETURN)
        constants.sleep_rand()
        self.browser.switch_to.window(self.browser.window_handles[1])
        constants.sleep_rand()

        # Profile Page Coding
        first_picture = self.browser.find_element_by_xpath(constants.paths["first_picture"])
        first_picture.click()
        
     

        constants.sleep_rand()
        exit_button = self.browser.find_element_by_xpath(constants.paths["exit_button"])
        like_button = self.browser.find_element_by_xpath(constants.paths["like_button"])
        comment_textarea = self.browser.find_element_by_xpath(constants.paths["comment_textarea"])
       

        
        constants.sleep_rand()
        print("liked photo")
        like_button.click()
        constants.sleep_rand()

        print("clicked on textarea")
        comment_textarea.click()
        constants.sleep_rand()
        comment_textarea = self.browser.find_element_by_xpath(constants.paths["comment_textarea"])
        # comment_textarea = self.browser.find_element_by_xpath('//textarea[@aria-label="Add a comment…"]')

        random_comment = constants.get_random_comment()
        for c in random_comment:
            comment_textarea.send_keys(c)
            sleep(0.1)
        # comment_textarea.send_keys(constants.get_random_comment())
        
        constants.sleep_rand()
        comment_post = self.browser.find_element_by_xpath(constants.paths["comment_post"])
        comment_post.click()
        print("comment posted")
        constants.sleep_rand()

        exit_button.click()
 
        

        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])



    def revert_messages(self, num_posts):
        # messages = browser.find_elements_by_xpath("//div[@class='Igw0E  Xf6Yq  eGOV_ ybXk5 _4EzTm']")
        
        
        messages = self.browser.find_elements_by_css_selector(constants.paths["messages"])[::-1]
        
        count = 0
        for m in messages:
            if count == num_posts:
                break
            count += 1 


            constants.sleep_rand()
            self.browser.execute_script("arguments[0].scrollIntoView(true)", m)

            # like_message = m.find_element_by_xpath(constants.paths["like_message"])
            # profile = m.find_element_by_xpath(constants.paths["profile"])

            # self.__like_comment(profile)

            # actions = ActionChains(self.browser)
            # actions.double_click(like_message).perform()
            

            
            try:
                
                like_message = m.find_element_by_xpath(constants.paths["like_message"])
                profile = m.find_element_by_xpath(constants.paths["profile"])

                self.__like_comment(profile)

                actions = ActionChains(self.browser)
                actions.double_click(like_message).perform()
            except:
                print("skipping non-emoji message")
            

           



