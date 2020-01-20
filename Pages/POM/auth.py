from selenium.webdriver.common.keys import Keys

from Locators.locators import LoginPageLocators
from Locators.locators import RegisterLocators


class Auth():

    def __init__(self, browser):
        self.browser = browser
        self.locator = LoginPageLocators
        self.locators_register = RegisterLocators

    def click_on_login_button(self):
        self.browser.click_on_element(self.locator.SIGNIN)

    def clean_login_field(self):
        self.browser.clean_element(self.locator.EMAIL_SIGNIN)

    def type_login(self, login):
        self.browser.send_keys_to_element(self.locator.EMAIL_SIGNIN, login)

    def clean_password_field(self):
        self.browser.clean_element(self.locator.PASSWORD)

    def type_pass(self, password):
        self.browser.send_keys_to_element(self.locator.PASSWORD, password)

    def press_button_signin(self):
        self.browser.click_on_element(self.locator.BUTTON_SIGIN)

    def click_register(self):
        self.browser.click_on_element(self.locators_register.REGISTER)

    def type_email_register(self, email):
        self.browser.send_keys_to_element(self.locators_register.EMAIL_SIGNIN, email)

    def type_password_register(self, password):
        self.browser.send_keys_to_element(self.locators_register.PASSWORD, password)

    def type_repassword_register(self, password):
        self.browser.send_keys_to_element(self.locators_register.RE_PASSWORD, password)
        self.browser.send_keys_to_element(self.locators_register.RE_PASSWORD, Keys.RETURN)
        self.browser.send_keys_to_element(self.locators_register.RE_PASSWORD, Keys.ESCAPE)

    def click_signin_tab(self):
        self.browser.click_on_element(self.locator.SIGNINTAB)




