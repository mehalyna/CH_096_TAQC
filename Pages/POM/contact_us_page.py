from Locators.locators import ContactUsPageLocators, NavigationMenuLocators
from Data.test_data import ContactUsData


class ContactUs():
    """Base functions for 'Contact us' page. Checking user communication with admin"""
    def __init__(self, browser):
        self.browser = browser
        self.menu_locator = NavigationMenuLocators
        self.locator = ContactUsPageLocators

    def check_type(self):
        """Selecting problem type from dropdown list"""
        self.browser.select_from_list_1(self.locator.LIST)

    def enter_description(self):
        """Entering description into field"""
        data = ContactUsData.DESCRIPTION_FOR_CONTACT
        self.browser.send_keys_to_element(self.locator.DESCRIPTION, data)

    def get_text_from_list(self):
        """Getting text from dropdown list"""
        self.browser.get_element_text(self.locator.TYPE)

    def get_text_from_result(self):
        """Getting text from a confirmation message"""
        res = self.browser.check_if_text_present(self.locator.MES, "Failed")
        return res

    def get_text_from_mes(self):
        """Getting text from message "Required" """
        res = self.browser.check_if_text_present(
            self.locator.REQUIRED, "Required")
        return res

    def get_text_from_desc(self):
        """Getting text from "Description" field. Checking if field full or empty"""
        res = self.browser.check_if_text_present(self.locator.DESCRIPTION, "")
        return res
