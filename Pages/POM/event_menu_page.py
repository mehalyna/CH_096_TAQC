import time
from Locators.locators import ProfilePageEventsMenuLocators, ProfileMenuPageHeaderInfoLocators


class EventsMenu:
    ''' Page object for events menu: ProfilePageEventsMenuLocators '''
    def __init__(self, browser):
        self.locator = ProfilePageEventsMenuLocators.locators_dict
        self.locator_info = ProfileMenuPageHeaderInfoLocators.locators_dict
        self.tab_dict = ProfilePageEventsMenuLocators.TAB_INDICATOR_DICT
        self.browser = browser

    def element_at_menu_bar_is_present(self, item_name, timeout):
        ''' Check the text attribute for an element as a criteria of existence '''
        result = self.browser.check_if_element_exists(self.locator[item_name], timeout)
        if result is not None:
            return True

    def get_text(self, item_name):
        ''' Verify text of the element (Header" user info).
        As an argument a string is used.'''
        return self.browser.get_element_text(self.locator_info[item_name])

    def get_text_tab(self, item_name):
        """
        Verify text of the element (tab from events menu).
        :Argument string:
        """
        print(self.tab_dict[item_name])
        return self.browser.check_if_element_exists(self.tab_dict[item_name])

    def count_event_menu_entries(self, container, item_name):
        '''Count items at the panel'''
        self.browser.click_on_element(self.locator[container])
        lst = self.browser.find_elements(self.locator[item_name])
        # ToDo count items at the panel

    def click_menu_item(self, item_name):
        """Clicking on an item using item_name (string type) which is selected from test_data.py
         'FUTURE EVENTS' ... 'ADD EVENT'
        The item_name is a key of dictionary of item locators
        """
        # self.browser.click_on_element(self.locator.ARCHIVE_EVENTS)
        self.browser.click_on_element(self.locator[item_name])

    def is_menu_item_active(self, item_name):
        """Check an tab item which is selected
        'FUTURE EVENTS' ... 'ADD EVENT'
        The item_name is a key of dictionary of item locators
        """
        self.browser.click_on_element(self.locator[item_name])
        return self.browser.visibility_of_element(self.tab_dict[item_name], timeout=5)

    def count_tabs(self, *locator):
        """ToDo In progress"""
        time.sleep(2)
        print(f"Locator for 'TABS_COUNT' is {locator}")
        # length = len(self.browser.find_elements(*self.locator['TABS_COUNT'])) + 1
        a = self.browser.get_list_element('button', *locator)
        length = len(a)
        # length = len(self.browser.check_if_element_exists(self.locator['FUTURE EVENTS']))
        # length = len(self.browser.find_elements_new()) + 1
        # content = driver.find_element_by_css_selector('p.content')
        return length

    def choose_last_event_but(self, *locator):
        a = self.browser.get_list_element('button', *locator)
        length = len(a)
        print(a)
        return length


# class EventsMenuCarts:
#     ''' CartPanelsAtProfilePageLocators '''
#     ''' Page object for events menu: ProfilePageEventsMenuLocators '''
#
#     def __init__(self, browser):
#         self.locator = CartPanelsAtProfilePageLocators.locators_dict
#         self.browser = browser
#
#     def element_at_menu_bar_is_present(self, item_name, timeout):
#         ''' Check the text attribute for an element as a criteria of existence '''
#         result = self.browser.check_if_element_exists(self.locator[item_name], timeout)
#         if result is not None:
#             return True

