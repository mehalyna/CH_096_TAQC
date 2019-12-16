import unittest
from Driver.driver import *
from Driver.driver import wrapper


class TestInit(unittest.TestCase):
    # Outdated
    def setUp(self):
        self.driver = wrapper(browser_setup["browser"])
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()




