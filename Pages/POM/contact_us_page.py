from Locators.locators import ContactUsPageLocators, NavigationMenuLocators
from Data.test_data import ContactUsData


class ContactUs():

    def __init__(self, browser):
        self.browser = browser
        self.menu_locator = NavigationMenuLocators
        self.locator = ContactUsPageLocators
        self.data = ContactUsData

    def enter_description(self, text):
        self.browser.send_keys_to_element(self.locator.DESCRIPTION, text)

    def click_on_submit(self):
        self.browser.click_on_element(self.locator.SUBMIT)

    def click_on_desc(self):
        self.browser.click_on_element(self.locator.DESCRIPTION)

    def click_on_clear(self):
        self.browser.click_on_element(self.locator.CLEAR)

    def get_element_text(self):
        a = self.browser.get_element_text(self.locator.MES)
        return a

    def check_type(self):
        self.browser.select_from_list(self.locator.LIST)

    def get_text_from_list(self):
        a = self.browser.get_element_text(self.locator.TYPE)
        return a







