from Driver.driver import browser_setup
from Base.base import BaseSetup
from Locator.locators import MainLoginPageLocators
from Data.TestData import TestData

# Outdated
class LoginPage(BaseSetup):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator_main = MainLoginPageLocators
        self.data = TestData

    def click_on_login_button(self):
        self.click_element(*self.locator_main.SIGNIN)

    def type_login(self, *login):
        self.send_keys_to(*login, *self.locator_main.EMAIL)

    def type_pass(self, *password):
        self.send_keys_to(*password, *self.locator_main.PASSWORD)

    def press_button_signin(self):
        ''' # form of signin /signup '''
        self.click_element(*self.locator_main.BUTTON_SIGIN)

    def login(self):
        self.click_on_login_button()
        self.type_login(self.data.LOGIN_USER)
        self.type_pass(self.data.PASSWORD_USER)
        self.press_button_signin()





