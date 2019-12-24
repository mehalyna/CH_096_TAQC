from Locators.locators import ProfilePageEventsMenuLocators


class EventsMenu:
    ''' Page object for events menu: ProfilePageEventsMenuLocators '''
    def __init__(self, browser):
        self.locator = ProfilePageEventsMenuLocators.locators_dict
        self.browser = browser

    def element_at_menu_bar_is_present(self, item_name, timeout):
        ''' Check the text attribute for an element as a criteria of existence '''
        result = self.browser.check_if_element_exists(self.locator[item_name], timeout)
        if result is not None:
            return True

    def get_text(self, item_name):
        ''' Verify text of the element (Header" user info)'''
        return self.browser.get_element_text(item_name)

    def count_event_menu_entries(self, container, item_name):
        self.browser.click_on_element(self.locator[container])
        lst = self.browser.find_elements(self.locator[item_name])
        # ToDo count items at the panel

    def click_menu_item(self, item_name):
        """Clicking on an item using item_name (string type) which is selected from test_data.py
         'FUTURE EVENTS'  'ARCHIVE EVENTS'  'VISITED EVENTS'  'ADD EVENT'

        The item_name is a key of dictionary of item locators
        """
        # self.browser.click_on_element(self.locator.ARCHIVE_EVENTS)
        self.browser.click_on_element(self.locator[item_name])



