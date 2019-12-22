from Driver.driver import browser_setup
from Base.base import BaseSetup
from Locators.locators import SearchEventPanelLocators
from selenium.webdriver.common.keys import Keys


class SearchPage(BaseSetup):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = SearchEventPanelLocators

    def type_in_search_field(self, data):
        self.clear_to_element(*self.locator.SEARCH_FIELD)
        self.send_keys_to_element(data, *self.locator.SEARCH_FIELD)

    def open_filter(self):
        self.click_to_element(*self.locator.BUTTON_MORE_FILTER)

    def enter_date_from(self, date):
        self.click_to_element(*self.locator.DATE_FROM)
        self.click_to_element(*self.locator.SELECT_DATE_FIELD)
        self.clear_to_element(*self.locator.SELECT_DATE_FIELD)
        self.send_keys_to_element(date, *self.locator.SELECT_DATE_FIELD)
        self.send_keys_to_element(Keys.ENTER, *self.locator.SELECT_DATE_FIELD)

    def enter_date_to(self, date):
        self.click_to_element(*self.locator.DATE_TO)
        self.click_to_element(*self.locator.SELECT_DATE_FIELD)
        self.clear_to_element(*self.locator.SELECT_DATE_FIELD)
        self.send_keys_to_element(date, *self.locator.SELECT_DATE_FIELD)
        self.send_keys_to_element(Keys.ENTER, *self.locator.SELECT_DATE_FIELD)

    def click_button_search(self):
        self.click_to_element(*self.locator.BUTTON_SEARCH)

    def click_button_reset(self):
        self.click_to_element(*self.locator.BUTTON_RESET)



