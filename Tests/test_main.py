import unittest
from selenium import webdriver
from Driver.driver import path
from Driver.browser_setup import browser_setup


class TestLoginToSite(unittest.TestCase):

    def setUp(self):
        if browser_setup["browser"] == "Firefox":
            self.driver = webdriver.Firefox(executable_path=path)
        elif browser_setup["browser"] == "Chrome":
            self.driver = webdriver.Chrome(executable_path=path)
        else:
            raise Exception("Selected browser not supported")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(browser_setup["url"])

    def tearDown(self):
        self.driver.close()
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()

