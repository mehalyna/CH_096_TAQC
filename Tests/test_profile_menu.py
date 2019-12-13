import unittest
from Driver.driver import *
from Driver.driver import wrapper
from Pages.eventsMenu import EventMenuPage
from Pages.LoginPage import LoginPage


class TestLoginToSite(unittest.TestCase):

    def setUp(self):
        self.driver = wrapper(browser_setup["browser"])
        # self.driver.delete_all_cookies()
        # self.driver.maximize_window()
        self.driver.get(browser_setup["url"])

    def tearDown(self):
        self.driver.quit()

    def test_event_menu(self):
        self.login_Page = LoginPage(self.driver)
        self.login_Page.login()

        # self.menu = EventMenuPage(self.driver)
        # self.activate_item()

if __name__ == '__main__':
    unittest.main()