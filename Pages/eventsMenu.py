from Driver.driver import browser_setup
from Base.base import BaseSetup
from Locator.locators import HomePageLocators
from Data.TestData import TestData


class EventMenuPage(BaseSetup):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData)
        self.locator_main = HomePageLocators


    def activate_item(self):
        # self.click_to_element(*self.locator_main.SIGNIN)
    # # Back to "Profile" menu
        self.driver.find_element(self.locator_main.PROFILE_SB).click()
    # time.sleep(pause)

    # def type_login(self, *login):
    #     self.send_keys_to(*login, *self.locator_main.EMAIL)

    # print('Back to "Profile" menu...')

    #
    # print("Moving on events groups menu...")
    # for i in range(5):
    #     css_sel = "#full-width-tab-{} > .MuiTab-wrapper".format(i)
    #     self.driver.find_element_by_css_selector(css_sel).click()
    #     time.sleep(pause)