import pytest
import time

from Driver.driver import Driver
from Data.test_data import Config
from utilities.start import InstantiatePages

# @pytest.fixture()
# def driver():
#     driver = Driver(Config.BROWSER).set_browser()
#     driver.delete_all_cookies()
#     # driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get(Config.HOME_URL)
#     # timeout = 2  # timeout
#     yield driver
#     time.sleep(3)  # ToDo
#     driver.close()
#     driver.quit()
#     # self.timeout = 0

# @pytest.fixture()
# def exec_instance():
#     exec_instance = InstantiatePages(driver)
#     yield exec_instance

