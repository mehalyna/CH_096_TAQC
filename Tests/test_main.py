import unittest
from selenium import webdriver
from Driver.driver import path
from Driver.driver import browser_setup
from Driver.driver import wrapper


class TestInit(unittest.TestCase):

    def setUp(self):
        self.driver=wrapper(browser_setup["browser"])
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(browser_setup["url"])
    #def tearDown(self):
    #    self.driver.quit()