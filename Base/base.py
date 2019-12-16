from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Base:

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

#     def do_click(self, locator):
#         self.do_find_element(locator).click()
#         # element.click()
#
#     def do_send_key(self, locator, key):
#         '''Fill in an element by a key'''
#
#         self.do_find_element(locator).send_keys(key)
#         # self.driver.find_element(By.NAME, 'btnK').submit()
#
#     def do_submit(self, locator, key):
#         '''Sumbits a key for selected element using a locator.
#         Returns an instance of ResultPage(self.driver)'''
#
#         self.driver.find_element(locator).submit(key)
#         # ToDo
#         # return ResultPage(self.driver)
#
#     def do_search(self, locator, arg):
#         '''Searching an arg within the element using a locator.
#         Returns an instance of ResultPage(self.driver)'''
#
#         self.do_find_element(locator).do_send_key(arg)
#         # self.driver.find_element(By.NAME, 'btnK').submit()
#         # ToDo
#         # return ResultPage(self.driver)
#
#     def do_get_text(self, locator):
#         '''Read and return a text from selected  by locator element'''
#
#         pass
#
#     def do_get_element_position(self, locator):
#         '''Get and return coordinate of selected element'''
#
#         pass
# =======
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







