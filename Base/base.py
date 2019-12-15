from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_find_element(self, locator, time = 10):
        ''' Explicit Waits method is used.
        Args: locator = tuple(By.selector, 'srt')
              waiting time = 10 # int()
        Returns instance of WebDriverWait on success within 10 secs or message
        for a rised exception.
        '''
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message = f"Can't find element by locator {locator}")

    def do_click(self, locator):
        self.do_find_element(locator).click()
        # element.click()

    def do_send_key(self, locator, key):
        '''Fill in an element by a key'''

        self.do_find_element(locator).send_keys(key)
        # self.driver.find_element(By.NAME, 'btnK').submit()

    def do_submit(self, locator, key):
        '''Sumbits a key for selected element using a locator.
        Returns an instance of ResultPage(self.driver)'''

        self.driver.find_element(locator).submit(key)
        # ToDo
        # return ResultPage(self.driver)

    def do_search(self, locator, arg):
        '''Searching an arg within the element using a locator.
        Returns an instance of ResultPage(self.driver)'''

        self.do_find_element(locator).do_send_key(arg)
        # self.driver.find_element(By.NAME, 'btnK').submit()
        # ToDo
        # return ResultPage(self.driver)

    def do_get_text(self, locator):
        '''Read and return a text from selected  by locator element'''

        pass

    def do_get_element_position(self, locator):
        '''Get and return coordinate of selected element'''

        pass





