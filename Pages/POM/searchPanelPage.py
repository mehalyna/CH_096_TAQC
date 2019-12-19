from selenium.webdriver.common.keys import Keys
from Locators.locators import SearchEventPanelLocators


class SearchEventMenu():

    def __init__(self, browser):
        self.browser = browser
        self.locator = SearchEventPanelLocators


    def type_in_search_field(self, date):
        self.browser.clean_element (self.locator.SEARCH_FIELD)
        self.browser.send_keys_to_element(self.locator.SEARCH_FIELD, date)

    def open_filter(self):
        self.browser.click_on_element(self.locator.BUTTON_MORE_FILTER)

    def enter_date_from(self, date):
        self.browser.click_on_element(self.locator.DATE_FROM)
        self.browser.click_on_element(self.locator.SELECT_DATE_FIELD)
        self.browser.clean_element(self.locator.SELECT_DATE_FIELD)
        self.browser.send_keys_to_element(self.locator.SELECT_DATE_FIELD, date)
        self.browser.send_keys_to_element(self.locator.SELECT_DATE_FIELD, Keys.ENTER)

    def enter_date_to(self, date):
        self.browser.click_on_element(self.locator.DATE_TO)
        self.browser.click_on_element(self.locator.SELECT_DATE_FIELD)
        self.browser.clean_element(self.locator.SELECT_DATE_FIELD)
        self.browser.send_keys_to_element(self.locator.SELECT_DATE_FIELD, date)
        self.browser.send_keys_to_element(self.locator.SELECT_DATE_FIELD, Keys.ENTER)

    def click_button_search(self):
        self.browser.click_on_element(self.locator.BUTTON_SEARCH)

    def click_button_reset(self):
        self.browser.click_on_element(self.locator.BUTTON_RESET)
    
    def check_element(self):
        return self.browser.get_element_text(self.locator.FIELD_NAME_EVENT)