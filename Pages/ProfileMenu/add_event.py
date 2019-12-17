from Locators.locators import CreateEvent
from Data.test_data import CreateEventData


class CreateEvents:

    def __init__(self, browser):
        self.browser = browser
        self.locator = CreateEvent
        self.data = CreateEventData


    def add_title(self,data):
        self.browser.clean_element( self.locator.EVENT_TITLE)
        self.browser.send_keys_to_element(self.locator.EVENT_TITLE,data)

    def upload_image(self):
        self.browser.upload_file(self.data.IMAGE, self.locator.UPLOAD_PICTURE)

    def add_desc(self,data):
        self.browser.clean_element( self.locator.DESC_TEXT )
        self.browser.send_keys_to_element(self.locator.DESC_TEXT, data)

    def add_categoty(self):
        pass


