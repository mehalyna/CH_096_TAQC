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
    exec = InstantiatePages(adriver)
    # do login
    exec.signin.enter_actor(CreateEventData.LOGIN_USER,
                                 CreateEventData.PASSWORD_USER)
    # go to Profile page
    exec.navigation.click_on_profile()

    yield adriver
    time.sleep(3)  # ToDo
    adriver.close()
    adriver.quit()
    # self.timeout = 0


# @pytest.fixture()
# def event(adriver):
#     selenium_test_base = InstantiatePages(driver)
#     yield selenium_test_base
