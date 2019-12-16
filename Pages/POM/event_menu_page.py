from Locators.locators import EventsMenuLocators


class EventsMenu:
    '''Page object for events menu'''
    def __init__(self, browser):
        self.locator = EventsMenuLocators.locators_dict
        self.browser = browser

    def click_item(self, item_name):
        """Clicking an item using item_name (string type) which is selected from test_data.py
        The item_name is a key of dictionary of item locators
        """
        if item_name in self.locator.keys():
            self.browser.click_on_element(self.locator[item_name])


