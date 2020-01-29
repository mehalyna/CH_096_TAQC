"""
Sign in module
"""
from Locators.locators import LoginPageLocators
from Locators.locators import RegisterLocators


class SignInUpClass:
    """
    Sign in scenario
    """

    def __init__(self, browser):
        self.browser = browser
        self.locator_login = LoginPageLocators
        self.locator_reg = RegisterLocators

    def enter_actor(self, username, password):
        """
        Sign in method as a scenario
        actor - is a person with own permissions (admin or user).
        Method of precondition for testing
        :param username: username
        :param password: pass phrase
        :return: login the EventExpress app
        """
        self.browser.click_on_element(self.locator_login.SIGNIN)
        self.browser.clean_element(self.locator_login.EMAIL_SIGNIN)
        self.browser.send_keys_to_element(self.locator_login.EMAIL_SIGNIN, username)
        self.browser.clean_element(self.locator_login.PASSWORD)
        self.browser.send_keys_to_element(self.locator_login.PASSWORD, password)
        self.browser.click_on_element(self.locator_login.BUTTON_SIGIN)
        print('Login OK')

    def click_sign_in_up(self):
        """
        on home page button for opening form with registration & login
        click on Signin button
        :return: None
        """
        self.browser.click_on_element(self.locator_login.SIGNIN)

    def click_on_register(self):
        """
        REGISTER FORM
        :return: None
        """
        self.browser.click_on_element(self.locator_reg.REGISTER)
