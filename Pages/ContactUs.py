from Driver.driver import browser_setup
from Base.base import BaseSetup
from Locator.locators import ContactUsPageLocators
from Tests.test_login import TestLogin


class ContactUsPage(BaseSetup):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ContactUsPageLocators

    def click_on_contact_us_tab(self):
        self.click_to_element(*self.locator.CONTACT_US)

    def enter_description(self, *description):
        self.send_keys_to(*description, *self.locator.DESCRIPTION)

    def click_on_submit(self):
        self.click_to_element(*self.locator.SUBMIT)

    def text_from_message(self):
        return self.text_from_elements(*self.locator.MESSAGE)
