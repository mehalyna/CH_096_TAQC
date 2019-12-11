from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Methods:
    '''Commonly used method '''

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        print(locator)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_elements(locator))
        return element

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def clear_element(self, locator):
        element = self.get_element(*locator)
        element.clear()

    def send_keys(self, locator, keys):
        elements = self.get_element(*locator)
        elements.send_keys(keys)
