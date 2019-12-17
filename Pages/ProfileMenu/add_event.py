from Locators.locators import CreateEvent


class CreateEvents:

    def __init__(self, browser):
        self.browser = browser
        self.locator = CreateEvent


    def add_title(self, data):
        self.browser.clean_element(self.locator.EVENT_TITLE)
        self.browser.send_keys_to_element(self.locator.EVENT_TITLE, data)
