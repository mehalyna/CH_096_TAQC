import pytest
from Base.base import BaseSetup
from selenium import webdriver
from Driver.driver import Driver
from Data.credentials import user,admin
# from Driver.browser_setup import browser_setup
from Data.test_data import Config
from utilities.testFrame import InitPagesDriver
import time  # ToDo



@pytest.fixture(scope='session')
def driver_init():
    driver = Driver(Config.BROWSER).set_browser()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Config.HOME_URL)
    return BaseSetup(driver)
     


@pytest.fixture(scope='function')
def app(driver_init):
    init_pages = InitPagesDriver(driver_init)


    def teardown():
        driver_init.driver.quit()
    return init_pages



@pytest.fixture(scope='function')
def get_to_user_profile(app):
    app.signin.enter_actor(admin['email'],admin['password'])
    

