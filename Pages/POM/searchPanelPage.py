from selenium.webdriver.common.keys import Keys
from Locators.locators import SearchEventPanelLocators as locator


class SearchEventMenu():
    """
    function for searching event on search panel
    """

    def __init__(self, browser):
        self.browser = browser


    def type_in_search_field(self, date):
        """clean search field and enter text
        :param date (str): text which you wand search"""
        self.browser.clean_element (locator.SEARCH_FIELD)
        self.browser.send_keys_to_element(locator.SEARCH_FIELD, date)

    def open_filter(self):
        """open filter-form"""
        self.browser.click_on_element(locator.BUTTON_MORE_FILTER)

    def enter_date_from(self, date):
        """
        Function enter date in field 'date from' 
        :param date ('mm/dd/year'): date 
        """
        self.browser.click_on_element(locator.DATE_FROM)
        self.browser.click_on_element(locator.SELECT_DATE_FIELD)
        self.browser.clean_element(locator.SELECT_DATE_FIELD)
        self.browser.send_keys_to_element(locator.SELECT_DATE_FIELD, date)
        self.browser.send_keys_to_element(locator.SELECT_DATE_FIELD, Keys.ENTER)

    def enter_date_to(self, date):
        """
        Function enter date in field 'date to'
        :param date ('mm/dd/year'): date 
        """
        self.browser.click_on_element(locator.DATE_TO)
        self.browser.click_on_element(locator.SELECT_DATE_FIELD)
        self.browser.clean_element(locator.SELECT_DATE_FIELD)
        self.browser.send_keys_to_element(locator.SELECT_DATE_FIELD, date)
        self.browser.send_keys_to_element(locator.SELECT_DATE_FIELD, Keys.ENTER)

    def click_button_search(self):
        """click button to search"""
        self.browser.click_on_element(locator.BUTTON_SEARCH)

    def click_button_reset(self):
        self.browser.click_on_element(locator.BUTTON_RESET)

    def click_to_categories(self):
        """click button to category and open list with categories"""
        self.browser.click_on_element(locator.HASHTAGS_FIELD)
        #self.browser.select_categoria_by_name(self.locator.HASHTAGS_SELECT, name)
        self.browser.get_list_element("innerHTML",locator.HASHTAGS_SELECT)

    def check_name_event(self):
        """Get name first event on the page"""
        return self.browser.get_element_text(locator.FIELD_NAME_EVENT)
