
import constants
from direct_message_page import DirectMessagePage


class HomePage: 
    def __init__(self,browser):
        self.browser = browser
        
        self.browser.implicitly_wait(constants.random_time())
        self.ignore_popups()

    def ignore_popups(self):
        
        save_info = self.browser.find_element_by_xpath(constants.paths["save_info"])
        save_info.click()
        constants.sleep_rand()

        notifications = self.browser.find_element_by_xpath(constants.paths["notifications"])
        notifications.click()
        constants.sleep_rand()

    def go_to_direct_messages(self):
        dm_button = self.browser.find_element_by_xpath(constants.paths["dm_button"])
        dm_button.click()
        return DirectMessagePage(self.browser)