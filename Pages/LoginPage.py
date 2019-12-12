from Driver.driver import browser_setup
from Base.base import BaseSetup
from Locator.locators import MainLoginPageLocators


class LoginPage(BaseSetup):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(browser_setup["url"])
        self.locator_main = MainLoginPageLocators

    def click_on_login_button(self):
        self.click_to_element( *self.locator_main.SIGNIN )

    def type_login(self, *login):
        self.send_keys_to( *login, *self.locator_main.EMAIL )

    def type_pass(self, *password):
        self.send_keys_to( *password, *self.locator_main.PASSWORD )

    def press_button_signin(self):
        self.click_to_element( *self.locator_main.BUTTON_SIGIN )




