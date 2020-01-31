from locators.locators import EventsMenuLocators, ProfileMenuPageHeaderInfoLocators


class EventsMenu:
    """
    Page object for events menu: ProfilePageEventsMenuLocators
    """

    def __init__(self, browser):
        self.locator = EventsMenuLocators.locators_dict
        self.locator_info = ProfileMenuPageHeaderInfoLocators.locators_dict
        self.tab_dict = EventsMenuLocators.TAB_INDICATOR_DICT
        self.browser = browser

    def element_at_menu_bar_is_present(self, item_name, timeout):
        """
        Check the text attribute for an element as a criteria of existence
        :param item_name: is a string - a name of an item
        :param timeout: timeout for wait of WebDriver
        :return: True if element is present at the menu bar and False on absence.
        """
        result = self.browser.check_if_element_exists(self.locator[item_name], timeout)
        if result is not None:
            return True

    def get_text(self, item_name):
        """
        Verify text of the element (Header" user info).
        As an argument a string is used.
        :param item_name: is a string - a name of an item
        :return: string of text
        """
        return self.browser.get_element_text(self.locator_info[item_name])

    def get_text_tab(self, item_name):
        """
        Verify text of the element (tab from events menu).
        :param item_name: string
        :return: True if element is exists and False - on absence.
        """
        return self.browser.check_if_element_exists(self.tab_dict[item_name])

    def click_menu_item(self, item_name):
        """
        Clicking on an item using item_name (string type) which is selected from test_data.py
        'FUTURE EVENTS' ... 'ADD EVENT'
        :param item_name: a key of dictionary of item locators
        """
        self.browser.click_on_element(self.locator[item_name])

    def is_menu_item_active(self, item_name):
        """
        Check an tab item which is selected
        'FUTURE EVENTS' ... 'ADD EVENT'
        The item_name is a key of dictionary of item locators
        :param item_name: a key of dictionary of item locators
        """
        self.browser.click_on_element(self.locator[item_name])
        return self.browser.visibility_of_element(self.tab_dict[item_name], timeout=5)

    def count_tabs(self, item_name):
        """
        :param item_name: is 'TABS_COUNT'
        :return integer: a number of entries of tabs
        Example of locator dictionary
            'TABS_COUNT': (By.CSS_SELECTOR, 'button[id*="full"]')
        """
        return len(self.browser.find_elements_new(self.locator[item_name]))
