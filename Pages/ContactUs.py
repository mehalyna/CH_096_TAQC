from Driver.driver import browser_setup
from Base.base import BaseSetup
from Locator.locators import ContactUsPageLocators
from Tests.test_login import Test_Login


class ContactUsPage(BaseSetup):

    def __init__(self, driver):
        super().__init__(driver)
        Test_Login.test_login_if_user_entered(self)
        self.locator_contact_us = ContactUsPageLocators

    def click_on_contact_us_tab(self):
        self.click_to_element(*self.locator_contact_us.CONTACT_US)

    def enter_description(self, *description):
        self.send_keys_to(*description, *self.locator_contact_us.DESCRIPTION)

    def click_on_submit(self):
        self.click_to_element(*self.locator_contact_us.SUBMIT)

    def text_from_message(self):
        return self.text_from_elements(*self.locator_contact_us.MESSAGE)
