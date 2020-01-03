from Locators.locators import ComunaPageLocators
from Locators.locators import SearchUsers
import time


class ComunaClass():


    def __init__(self, browser):
        self.browser = browser
        self.loc_comuna = ComunaPageLocators
        self.loc_search = SearchUsers


    def chose_respond(self,name):
        """
        method for chose user for communication (exchange messages)
        :param name: name of user who writing for
        :return:
        """
        self.browser.send_keys_to_element(self.loc_search.FIELD_SEARCH,name)
        time.sleep(2)
        self.browser.click_on_element(self.loc_search.SEARCH)
        self.browser.click_on_element(self.loc_search.NAME_USERS)

    def check_received_msg(self):
        lst = self.browser.get_element_text(self.loc_comuna.MSG_RECEIVED)
        print(lst)
