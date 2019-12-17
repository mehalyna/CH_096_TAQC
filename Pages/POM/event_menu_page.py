from Locators.locators import ProfilePageEventsMenuLocators


class EventsMenu:
    '''Page object for events menu'''
    def __init__(self, browser):
        self.locator = ProfilePageEventsMenuLocators.locators_dict  # dict to be implemented later ToDo
        self.browser = browser

    def count_event_menu_entries(self, container, item_name):
        self.browser.click_on_element(self.locator[container])
        lst = self.browser.find_elements(self.locator[item_name])
        # ToDo count items at the panel

    def click_menu_item(self, item_name):
        """Clicking an item using item_name (string type) which is selected from test_data.py
         'FUTURE EVENTS'  'ARCHIVE EVENTS'  'VISITED EVENTS'  'ADD EVENT'

        The item_name is a key of dictionary of item locators
        """
        # self.browser.click_on_element(self.locator.ARCHIVE_EVENTS)

        if item_name in self.locator.keys():
            self.browser.click_on_element(self.locator[item_name])


