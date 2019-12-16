import unittest
from selenium import webdriver
from Driver.driver import Driver
# from Driver.browser_setup import browser_setup
from Data.test_data import Config
from utilities.testFrame import InitPagesDriver


class TestInit(unittest.TestCase):

    def setUp(self):
        # if browser_setup["browser"] == "Firefox":
        #     self.driver = webdriver.Firefox(executable_path=path)
        # elif browser_setup["browser"] == "Chrome":
        #     self.driver = webdriver.Chrome(executable_path=path)
        # else:
        #     raise Exception("Selected browser not supported")
        self.driver = Driver(Config.BROWSER).setBrowser()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Config.HOME_URL)

        self.exec = InitPagesDriver(self.driver)


    # def tearDown(self):
    #     self.driver.close()
    #     self.driver.quit()




if __name__ == '__main__':
    unittest.main()

