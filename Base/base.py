from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BaseSetup:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locators):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_element(*locators))
        return element

    # def element_be_clickable(self, *locator):
    #     try:
    #         wait = WebDriverWait( self.driver, 5)
    #         element = wait.until(EC.element_to_be_clickable(*locator))
    #         return element
    #     except NoSuchElementException:
    #      pass

    # def wait_apeare_disapeare(self, *locator):







    def click_on_element(self, locators):
        element = self.find_element(*locators)
        element.click()

    def clean_element(self, locators):
        element = self.find_element(*locators)
        element.clear()


    def send_keys_to_element(self, locators, data):
        element = self.find_element(*locators)
        element.send_keys(data)


    def upload_file(self, path, locators):
        element = self.find_element(locators)
        element.send_keys(path)



    def element_be_clickable(self, *locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(*locator))















