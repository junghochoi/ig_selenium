
import constants
import os 



from dotenv import  load_dotenv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from login_page import LoginPage


def main():

    load_dotenv()
    SECONDS = 15
    NUM_MESSAGES = int(input("Num Posts to revert: "))
    USERNAME = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")

    browser = webdriver.Firefox()
    constants.sleep_rand()

    login_page = LoginPage(browser)
    constants.sleep_rand()
    
    home_page = login_page.login(USERNAME, PASSWORD)
    constants.sleep_rand()


    dm_page = home_page.go_to_direct_messages()
    dm_page.go_to_small_business()
    


    dm_page.load_messages(SECONDS)
    dm_page.revert_messages(NUM_MESSAGES)


    print("Script has finished")



main()