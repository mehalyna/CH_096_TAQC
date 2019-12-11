from Pages.Page import Methods
from Locators.locators import Locators_Login

class LoginPage(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators_Login()

    def click_signin(self):
        self.click_element(self.locator.signin)

    # def click_enter(self):
    #     self.driver.find_element(*self.log.enter).click()
    #
    # def enter_username(self, username):
    #     self.driver.find_element(*self.log.username).clear()
    #     self.driver.find_element(*self.log.username).send_keys(username)
    #
    # def enter_password(self, password):
    #     self.driver.find_element(*self.log.password).clear()
    #     self.driver.find_element(*self.log.password).send_keys(password)