from selenium.webdriver.common.keys import Keys

from locators.locators import LoginPageLocators
from locators.locators import RegisterLocators


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

    def send_escape(self):
        self.browser.send_keys_to_element(self.locators_register.RE_PASSWORD, Keys.ESCAPE)

    def click_signin_tab(self):
        self.browser.click_on_element(self.locator.SIGNINTAB)

    def check_warning_message_about_existing_email(self):
        return self.browser.find_element_by_xpath("//div[2]/p").text

    def check_warning_message_about_invalid_email(self):
        return self.browser.find_element_by_xpath("(//div[1]/div/p)[2]").text

    def check_warning_message_about_invalid_password(self):
        return self.browser.find_element_by_xpath("//div[2]/div/p").text

    def fill_register_data(self, email, password):
        self.click_on_login_button()
        self.click_register()
        self.type_email_register(email)
        self.type_password_register(password)
        self.type_repassword_register(password)

    def fill_login_data(self, email, password):
        self.click_on_login_button()
        self.click_signin_tab()
        self.clean_login_field()
        self.type_login(email)
        self.clean_password_field()
        self.type_pass(password)
        self.press_button_signin()
