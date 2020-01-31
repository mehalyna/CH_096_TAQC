from locators.locators import Comuna


class Comunication():

    def __init__(self, browser):
        self.browser = browser
        self.comuna_locators = Comuna

    def click_on_comuna(self):
        self.browser.click_on_element(self.comuna_locators.COMUNA_NAV)

    def click_on_user_dialog(self):
        self.browser.click_on_element(self.comuna_locators.USER_TEST_DIALOG)

    def click_send(self):
        self.browser.click_on_element(self.comuna_locators.SEND)

    def type_message(self, message):
        self.browser.send_keys_to_element(self.comuna_locators.DIALOG_INPUT, message)

    def get_text_of_notify(self):
        return self.browser.find_element_by_xpath("//span[@class = 'text-info']").text





