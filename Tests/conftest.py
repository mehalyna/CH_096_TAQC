import pytest
import time

from Driver.driver import Driver
from Data.test_data import Config


# @pytest.fixture(scope="session")
# def driver(self):
#     self.driver = Driver(Config.BROWSER).set_browser()
#     self.driver.delete_all_cookies()
#     # self.driver.maximize_window()
#     self.driver.implicitly_wait(10)
#     self.driver.get(Config.HOME_URL)
#     yield self.driver, self.exec
#     time.sleep(3)  # ToDo
#     self.driver.close()
#     self.driver.quit()
#
#     self.timeout = 0