# import unittest
import pytest
from selenium import webdriver
from Driver.driver import Driver
# from Driver.browser_setup import browser_setup
from Data.test_data import Config
from utilities.testFrame import InitPagesDriver
import time  # ToDo



class TestInit():
    pass

    # @pytest.fixture()
    # def test_setup(self):
    #     self.driver = Driver(Config.BROWSER).set_browser()
    #     self.driver.delete_all_cookies()
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)
    #     self.driver.get(Config.HOME_URL)
    #     self.exec = InitPagesDriver(self.driver)
    #
    #     yield
    #     time.sleep(3)  # ToDo
    #     self.driver.close()
    #     self.driver.quit()
    #     return self

    # @pytest.fixture
    # def firefox_options(firefox_options):
    #     firefox_options.binary = '/path/to/firefox-bin'
    #     firefox_options.add_argument('-foreground')
    #     firefox_options.set_preference('browser.anchor_color', '#FF0000')
    #     return firefox_options

    # def setUp(self):
    #     self.driver = Driver(Config.BROWSER).set_browser()
    #     self.driver.delete_all_cookies()
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)
    #     self.driver.get(Config.HOME_URL)
    #
    #     self.exec = InitPagesDriver(self.driver)





# if __name__ == '__main__':
#     pytest.main()

