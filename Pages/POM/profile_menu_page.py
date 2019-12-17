from Locators.locators import ProfileMenuLocators


# profile page directed from navigation menu
class ProfileMenu():

    def __init__(self,browser):
        self.browser = browser
        self.locator = ProfileMenuLocators


    def click_on_add_event(self):
        self.browser.click_on_element(self.locator.ADD_EVENT)