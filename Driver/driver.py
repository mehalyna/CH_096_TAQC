# import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager


class Driver:
    '''Wrapped based on https://github.com/SergeyPirogov/webdriver_manager/tree/master
    Provides automatically manage of drivers for different browsers'
    It's on https://pypi.org/project/webdriver-manager/
    Installation:
        pip install webdriver-manager
    Desired.Capabilities will be implemented in the future'
    '''

    def __init__(self, browser):
        self.browser = browser

    def setBrowser(self):
        if self.browser.lower() == "firefox":
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser.lower() == "chrome":
            return webdriver.Chrome(ChromeDriverManager().install())
        elif self.browser.lower() == "opera":
            return webdriver.Opera(executable_path=OperaDriverManager().install())
        elif self.browser.lower() == "opera":
            return webdriver.Opera(executable_path=OperaDriverManager().install())
        elif self.browser.lower() == "ie":
            return webdriver.Ie(IEDriverManager().install())
        else:
            raise Exception("Selected browser not supported")
