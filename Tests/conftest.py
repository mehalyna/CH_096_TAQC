import pytest
from selenium import webdriver
from Driver.driver import Driver
from Base.base import BaseSetup
from Data.test_data import Config
from utilities.testFrame import InitPagesDriver
import time  # ToDo



@pytest.fixture(scope = 'function')
def browser_init(self):
    '''Browser init'''
    driver = Driver(Config.BROWSER).set_browser()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Config.HOME_URL)
    yield
    time.sleep(10)
    driver.close()
    driver.quit()
    browser = BaseSetup(driver)

#@pytest.fixture(score='function')
#def app(self):
#    return browser
#    self.driver.close()
#    self.driver.quit()




