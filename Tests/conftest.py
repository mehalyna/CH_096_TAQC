import pytest
from Driver.driver import Driver
from Data.test_data import Config
from utilities.testFrame import InitPagesDriver


@pytest.fixture(scope="session")
def browser():
    # driver = webdriver.Chrome(executable_path="./chromedriver")
    # yield driver
    # driver.quit()
    driver = Driver(Config.BROWSER).set_browser()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Config.HOME_URL)
    yield driver
    driver.quit()

# test example
# from YandexPages import SearchHelper
#
# def test_yandex_search(browser):
#     yandex_main_page = SearchHelper(browser)
#     yandex_main_page.go_to_site()
#     yandex_main_page.enter_word("Hello")
#     yandex_main_page.click_on_the_search_button()
#     elements = yandex_main_page.check_navigation_bar()
#     assert "Картинки" and "Видео" in elements



# Pages example
# from BaseApp import BasePage
# from selenium.webdriver.common.by import By
#
#
# class YandexSeacrhLocators:
#     LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
#     LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
#     LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
#
#
# class SearchHelper(BasePage):
#
#     def enter_word(self, word):
#         search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
#         search_field.click()
#         search_field.send_keys(word)
#         return search_field
#
#     def click_on_the_search_button(self):
#         return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON,time=2).click()
#
#     def check_navigation_bar(self):
#         all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
#         nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
#         return nav_bar_menu

# BaseApp example
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class BasePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.base_url = "https://ya.ru/"
#
#     def find_element(self, locator,time=10):
#         return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
#                                                       message=f"Can't find element by locator {locator}")
#
#     def find_elements(self, locator,time=10):
#         return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
#                                                       message=f"Can't find elements by locator {locator}")
#
#     def go_to_site(self):
#         return self.driver.get(self.base_url)