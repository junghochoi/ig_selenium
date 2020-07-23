
from selenium import webdriver
from home_page import HomePage
import constants
class LoginPage:

    def __init__(self,browser):
        self.browser = browser
        self.browser.implicitly_wait(constants.random_time())
        browser.get("https://instagram.com/")
    
    def login(self, username, password):
        username_input = self.browser.find_element_by_xpath(constants.paths["username_input"])
        password_input = self.browser.find_element_by_xpath(constants.paths["password_input"])
        login_button   = self.browser.find_element_by_xpath(constants.paths["login_button"])

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()  
        
        return HomePage(self.browser)
