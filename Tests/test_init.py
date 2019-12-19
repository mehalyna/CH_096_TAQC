import unittest
from selenium import webdriver
from Driver.driver import Driver
# from Driver.browser_setup import browser_setup
from Data.test_data import Config
from utilities.testFrame import InitPagesDriver
import time  # ToDo



class TestInit(unittest.TestCase):


    def setUp(self):
        self.driver = Driver(Config.BROWSER).set_browser()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Config.HOME_URL)

        self.exec = InitPagesDriver(self.driver)

    def tearDown(self):
            time.sleep(3)  # ToDo
            self.driver.close()
            self.driver.quit()



if __name__ == '__main__':
    unittest.main()

