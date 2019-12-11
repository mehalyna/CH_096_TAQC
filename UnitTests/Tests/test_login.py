import unittest
from selenium import webdriver
import time
from Pages.LoginPage import LoginPage
from Tests.testdata import *

class LoginTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print('setupClass')
    #     cls.driver = webdriver.Chrome(r'C:/Users/bskiptc/Documents/chromedriver')
    #     # cls.driver = webdriver.Chrome(r'/home/boris/Apps/chromedriver')
    #     cls.driver.implicitly_wait(10)
    #     # cls.driver.maximize_window()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass')
    #     cls.driver.close()
    #     cls.driver.quit()

    def setUp(self):
        print('setUp')
        self.driver = webdriver.Chrome(r'C:\Users\bskiptc\Documents\chromedriver')
        # self.driver.maximize_window()
        self.driver.implicitly_wait(4)
        # ToDo
        self.driver.get(HOME)

        # self.homepage = HomePage(self.driver)
        # self.driver.title

    def tearDown(self):
        # print('tearDown')
        self.driver.close()

    def test_login(self):
        loginObj = LoginPage(self.driver)
        loginObj.click_signin()


if __name__ == '__main__':
    unittest.main()
