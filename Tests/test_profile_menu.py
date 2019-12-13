import unittest
from Driver.driver import *
from Driver.driver import wrapper
from Pages.eventsMenu import EventMenuPage
from Pages.LoginPage import LoginPage
from Data.TestData import TestData


class TestInit(unittest.TestCase):

    def setUp(self):
        self.driver = wrapper(browser_setup["browser"])
        self.driver.get(browser_setup["url"])

    def tearDown(self):
        self.driver.quit()

    def test_event_menu(self):
        self.login_Page = LoginPage(self.driver)
        self.login_Page.login()

        self.menu = EventMenuPage(self.driver)
        # self.menu.activate_item()

if __name__ == '__main__':
    unittest.main()