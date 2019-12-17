from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BaseSetup:

    def __init__(self,driver):
        self.driver = driver

    def find_element(self, *locators):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_element(*locators))
        return element

    def element_be_clickable(self, *locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable(*locator))
            return element
        except TimeoutException as e:
            print('Element is not clickable')
            return ''


    # def wait_apeare_disapeare(self, *locator):







    def click_on_element(self,locators):
        element = self.find_element(*locators)
        element.click()

    def clean_element(self,locators):
        element = self.find_element(*locators)
        element.clear()


    def send_keys_to_element(self, locators,data):
        element = self.find_element(*locators)
        element.send_keys(data)

    #search text that displayed in element (form)
    def get_element_text(self, locator):
        element = self.find_element(*locator)
        print(element.text)
        return element.text


    # check if text present in element. Return True or print message

    def check_if_text_present(self, *locators, text=None):
        error_msg = "Text not found not found "
        try:
            wait = WebDriverWait(self.driver, 5)
            text_get = wait.until(EC.text_to_be_present_in_element(*locators), text)
            return text_get
        except TimeoutException:
            print(error_msg)
            return ''




    def upload_file(self, path, locators):
        element = self.find_element(*locators)
        element.send_keys(path)










    def check_if_text_present(self, *locators, text=None):
        error_msg = "Text not found"
        try:
            wait = WebDriverWait(self.driver, 5)
            text_get = wait.until(EC.text_to_be_present_in_element(*locators), text)
            return text_get
        except TimeoutException:
            print(error_msg)
            return ''















