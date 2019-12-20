from selenium.webdriver.common.keys import Keys
from Locators.locators import SearchEventPanelLocators


class SearchEventMenu():
    """
    function for searching event on search panel
    """

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

    def click_to_categories(self):
        self.browser.click_on_element(self.locator.HASHTAGS_FIELD)
        #self.browser.select_categoria_by_name(self.locator.HASHTAGS_SELECT, name)
        self.browser.get_list_element("innerHTML",self.locator.HASHTAGS_SELECT)

    def check_name_event(self):
        return self.browser.get_element_text(self.locator.FIELD_NAME_EVENT)
