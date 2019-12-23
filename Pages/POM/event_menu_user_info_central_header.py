from Locators.locators import ProfileMenuPageHeaderInfoLocators

from Base.base import BasePage


class ProfileEventsCentralHeaderUserInfo():
    ''' Page object element for events carts panel: CartPanelsAtProfilePageLocators '''

    def __init__(self, browser):
        self.locator = ProfileMenuPageHeaderInfoLocators  # .locators_dict
        self.browser = browser

    # def check_item_text(self, locator, text_to_find_and_check):
    #     error_msg = f"Failed: expected result '{text_to_find_and_check}' doesn't match actual result "
        # self.browser.
        # self.assertTrue(self.exec.base.check_if_text_present(self.locator.USER_NAME_LABEL, error_msg)), "not equal"

    # def count_event_menu_entries(self, container, item_name):
    #     self.browser.click_on_element(self.locator[container])
    #     lst = self.browser.find_elements(self.locator[item_name])
    #     # ToDo count items at the panel
