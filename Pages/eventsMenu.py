from Base.base import Base
from Locators.locators import HomePageLocators
from Data.test_data import Config
from selenium.webdriver.common.by import By

import time

class EventMenuPage(Base):
    # Outdated version
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_main = HomePageLocators


    def activate_item(self):
    # # Back to "Profile" menu
         self.click_element(*self.locator_main.PROFILE)
        # self.find_element(self.locator_main.PROFILE)
        #  self.click_element(*self.locator_main.PROFILE)
        #
        # print("Moving on events of a group menu...")
        #  for i in range(5):
        #     css_sel = "#full-width-tab-{} > .MuiTab-wrapper".format(i)
        #     self.find_element(By.CSS_SELECTOR, css_sel)
        #     time.sleep(2)

    # def click_on_login_button(self):
    #     self.click_element(*self.locator_main.SIGNIN)
    #
    # def type_login(self, *login):
    #     self.send_keys_to(*login, *self.locator_main.EMAIL)
    #
    # def type_pass(self, *password):
    #     self.send_keys_to(*password, *self.locator_main.PASSWORD)
    #
    # def press_button_signin(self):
    #     ''' # form of signin /signup '''
    #     self.click_element(*self.locator_main.BUTTON_SIGIN)