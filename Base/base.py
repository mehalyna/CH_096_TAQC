import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class BaseSetup():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locators):
        """
        Wrapper for  common selenium method find_element.Used explicit
        wait for finding element
        :param locators: css locator or xpath
        :return: webElement
        """
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(
            lambda driver: self.driver.find_element(
                *locators))
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            lambda driver: self.driver.find_element(
                *locators))
        return element

    def find_elements(self, *locators):
        """
         Wrapper for  common selenium method find_element.Used explicit
         wait for finding elements.Used explicit
         wait for finding element
         :param locators: css selector or xpath
         :return: webElements
        """
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(
            lambda driver: self.driver.find_elements(
                *locators))
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            lambda driver: self.driver.find_elements(
                *locators))
        return element

    def find_element_by_tag(self, tag):
        """
        Wrapper for selenium method find_elements_by_tag_name
        :param tag: tag of web element
        :return: webElement
        """
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(
            lambda driver: self.driver.find_elements_by_tag_name(tag))
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            lambda driver: self.driver.find_elements_by_tag_name(tag))
        return element

    def find_element_by_xpath(self, xpath):
        """
        Wrapper for selenium method find_element_by_xpath
        :param xpath: xpath
        :return: webElement
        """
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(
            lambda driver: self.driver.find_element_by_xpath(xpath))
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            lambda driver: self.driver.find_element_by_xpath(xpath))
        return element

    def click_on_element(self, locators):
        """
        Wrapper for selenium method click(). Finding element and make click for it
        :param locators: css selector or xpath
        :return: None
        """
        element = self.find_element(*locators)
        element.click()

    def clean_element(self, locators):
        """
        Wrapper for common selenium method .clear().
        Finding web form (example textfield, upload, download )
        and clean text or other data inside
        :param locators: css selector or xpath
        :return: None
        """
        element = self.find_element(*locators)
        element.clear()

    def send_keys_to_element(self, locators, data):
        """
        Wrapper for common selenium  method
        :param locators: css selector or xpath
        :param data: text, or file or picture(.jpg,png)
        :return: None
        """
        element = self.find_element(*locators)
        element.send_keys(data)

    def get_list_element(self, ele_html: str, *locators):
        """
        Method for getting values from list of webElements(li, tr ....)
        Used Explicit Wait
        :param ele_html: example - li, tr, td etc.
        :param locators: css selector or xpath
        :return: list of values of html_element
        """
        wait = WebDriverWait(self.driver, 30)
        lst = (
            list(
                lst_cat.get_attribute(ele_html)for lst_cat in wait.until(
                    EC.visibility_of_all_elements_located(
                        *
                        locators))))
        """get list of elements li, tr ...."""
        wait = WebDriverWait(self.driver, 10)
        lst = (
            list(
                lst_cat.get_attribute(ele_html)for lst_cat in wait.until(
                    EC.visibility_of_all_elements_located(
                        *
                        locators))))
        return lst

    def select_from_list(self, locator_1):
        """
        Method finding (webElement) tag SELECT
        :param locator_1: css selector or xpath
        :return: random element from SELECT  (drop-down menu/list)
        """
        sel = Select(self.find_element(*locator_1))
        choice = random.choice([c.text for c in sel.options])
        return choice

    def select_from_list_1(self, locator_1):
        """
        Method finding (webElement) tag SELECT
        :param locator_1: css selector or xpath
        :return: random element from SELECT  (drop-down menu/list)
        """
        sel = self.find_element(*locator_1)
        a = Select(sel)
        choice = random.choice([c.text for c in a.options])
        return a.select_by_visible_text(choice)

    def click_action(self, x, y):
        """
        Wrapper for selenium common.action_chains.Method implement click on coordinate
        :param x: coordinate x
        :param y: coordinate y
        :return: None
        """
        action = ActionChains(self.driver)
        action.move_by_offset(x, y).click().perform()

    def element_be_clickable(self, *locator):
        """
        Wrapper for common selenium method. Function finding webElement and check
        if  element is click able. If False- printing error message
        :param locator:
        :return:
        """
        try:
            wait = WebDriverWait(self.driver, 30)
            element = wait.until(EC.element_to_be_clickable(*locator))
            return element
        except TimeoutException as e:
            print('Element is not clickable')
            return ''

    def scroll_to_element(self, locators):
        """
        Wrapper for selenium method scroll to element
        :param locators: css selector or xpath
        :return: scroll to element and return coordinates

        """
        element = self.find_element(*locators)
        return element.location_once_scrolled_into_view

    def upload_file(self, path, locators):
        """

        :param path: absolute path to dir with file or picture
        :param locators: css locator or xpath
        :return: None
        """
        element = self.find_element(*locators)
        element.send_keys(path)

    def get_element_text(self, locator):
        """
        Method for getting text from webElement
        :param locator: css locator or xpath
        :return: text
        """
        element = self.find_element(*locator)
        a = element.text
        wait = WebDriverWait(self.driver, 5)
        print(a)
        return a

    # check if text present in element. Return True or print message
    def check_if_text_present(self, *locators, text=None):
        """
        Method for finding text on web element
        :param locators:css locator or xpath
        :param text: text with no value
        :return: text or False
        """

        error_msg = "Text not found"
        try:
            wait = WebDriverWait(self.driver, 5)
            text_get = wait.until(
                EC.text_to_be_present_in_element(
                    *locators), text)
            return text_get
        except TimeoutException:
            print(error_msg)
            return False

    def check_if_element_exists(self, locator, timeout=5):
        ''' Check the text attribute for an element as a criteria of existence.
        Args: locator = tuple(By.selector, 'srt')
              waiting time = 10 # int()
        Returns text of element on success within timeout interval or
        an empty string and print a message for a raised exception.
        Explicit Waits method is used.
        '''

        alert = f"Can't find element by locator {locator}"
        try:
            element = WebDriverWait(self.driver, timeout)\
                .until(EC.presence_of_element_located(locator),
                       message=alert)
            text_get = element.text
            return text_get
        except TimeoutException:
            print(alert)
            return None

    def select_categoria_by_name(self, locator, text):
        """
        Click on web element in drop down menu
        :param locator: css selector or xpath
        :param text: text
        :return:
        """""
        select = Select(self.driver.find_element(*locator))
        elem = select.select_by_visible_text(text)
        elem.click()
