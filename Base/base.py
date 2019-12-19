from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import time



class BaseSetup():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locators):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_element(*locators))
        return element

    def find_element_by_tag(self, tag):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_elements_by_tag_name(tag))
        return element

    def find_element_by_xpath(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_element_by_xpath(xpath))
        return element
    # def element_be_clickable(self, *locator):
    #     try:
    #         wait = WebDriverWait( self.driver, 5)
    #         element = wait.until(EC.element_to_be_clickable(*locator))
    #         return element
    #     except NoSuchElementException:
    #      pass

    # def wait_apeare_disapeare(self, *locator):



    def click_to_element(self, *locators):
        element = self.find_element(*locators)
        element.click()

    def clear_to_element(self, *locators):
        element = self.find_element(*locators)
        element.clear()

    def element_be_clickable(self, *locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable(*locator))
            return element
        except TimeoutException as e:
            print('Element is not clickable')
            return ''

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

    def get_element_text(self, locator):
        element = self.find_element(*locator)
        print(element.text)
        return element.text

    # check if text present in element. Return True or print message
    def check_if_text_present(self, *locators, text=None):
        error_msg = "Text not found"
        try:
            wait = WebDriverWait(self.driver, 5)
            text_get = wait.until(EC.text_to_be_present_in_element(*locators), text)
            return text_get
        except TimeoutException:
            print(error_msg)
            return ''

    def select_from_list(self, locator_1):
        sel = self.find_element(*locator_1)
        a = Select(sel)
        choice = random.choice([c.text for c in a.options])
        return a.select_by_visible_text(choice)

    def select_categoria_by_name(self, locator, text):
        """get and click to field in dropdown menu"""
        select = Select(self.driver.find_element(*locator))
        elem = select.select_by_visible_text(text)
        elem.click()

    def get_list_element(self, ele_html: str, *locators):
        wait = WebDriverWait(self.driver, 10)
        lst = (list(lst_cat.get_attribute(ele_html)for lst_cat in wait.until(EC.visibility_of_all_elements_located(*locators))))
        print (lst)
        return lst





