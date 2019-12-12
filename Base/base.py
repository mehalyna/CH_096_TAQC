from selenium.webdriver.support.ui import WebDriverWait

class BaseSetup():

    def __init__(self,driver):
        self.driver = driver

    def find_element(self, *locators):
        wait = WebDriverWait( self.driver, 10 )
        element = wait.until(lambda driver: self.driver.find_element( *locators))
        return element

    def click_to_element(self, *locators):
        element = self.find_element(*locators)
        element.click()

    def clear_to_element(self, *locators):
        element = self.find_element(*locators)
        element.clear()

    def send_keys_to(self,data,*locators):
        element = self.find_element(*locators)
        element.send_keys(data)




