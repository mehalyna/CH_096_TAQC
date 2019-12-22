import pytest
import time

from Driver.driver import Driver
from Data.test_data import Config
from utilities.start import InstantiatePages
from Data.test_data import CreateEventData


@pytest.fixture(scope='function')
def driver():
    adriver = Driver(Config.BROWSER).set_browser()
    adriver.delete_all_cookies()
    # self.driver.maximize_window()
    adriver.implicitly_wait(10)
    adriver.get(Config.HOME_URL)
    timeout = 1  # timeout
    # do instantiate all classes
    obj = InstantiatePages(adriver)
    # do login
    obj.signin.enter_actor(CreateEventData.LOGIN_USER,
                                 CreateEventData.PASSWORD_USER)
    # go to Profile page
    obj.navigation.click_on_profile()

    yield adriver
    time.sleep(3)  # ToDo
    adriver.close()
    adriver.quit()
    # self.timeout = 0

'''
@pytest.fixture(scope='function')
def get_driver():
    print('===============setUp===================')
    driver = Driver(Config.BROWSER).set_browser()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Config.HOME_URL)
    obj = BaseSetup(driver)
    return obj

    # def teardown_module(self):
    #     print('===============teardown===================')
    #     time.sleep(3)  # ToDo
    #     driver.close()
    #     driver.quit()

@pytest.fixture(scope='function')
def event(get_driver):
    event_init = InitPagesDriver(get_driver)
    return event_init
'''
