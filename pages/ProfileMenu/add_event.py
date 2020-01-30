from locators.locators import CreateEvent
from data.test_data import CreateEventData
from selenium.webdriver.common.keys import Keys
import random

event = CREATE_EVENT


class CreateEvents():

    def __init__(self, browser):
        self.browser = browser
        self.locator = CreateEvent

    def add_title(self, data):
        """
        Method for adding title
        :param data: title -> str
        :return:
        """
        self.browser.clean_element(self.locator.EVENT_TITLE)
        self.browser.send_keys_to_element(self.locator.EVENT_TITLE, data)

    def upload_image(self):
        """
        Method for uploading
        :return: None
        """
        self.browser.upload_file(event['image'], self.locator.UPLOAD_PICTURE)

    def add_desc(self, data):
        """
        Method for adding description to event
        :param data: text -> str
        :return:
        """
        self.browser.clean_element(self.locator.DESC_TEXT)
        self.browser.send_keys_to_element(self.locator.DESC_TEXT, data)

    def add_date(self, data):
        """
        Add date from to event
        :param data:
        :return:
        """
        self.browser.click_on_element(self.locator.CALENDAR)
        self.browser.clean_element(self.locator.CALENDAR_VALUE)
        self.browser.send_keys_to_element(self.locator.CALENDAR_VALUE, data)

    # n - it's number of categories
    # will be add. In test we must import module random
    # adding will start after click on field category
    def add_category_random(self, *locator_cat):
        """
        n - it's number of categories
        will be add. In test we must import module random
        adding will start after click on field category
        :param locator_cat: css selector or xpath
        :return:
        """
        n = random.randint(1, 4)
        while n > 0:
            lst = self.browser.get_list_element("innerHTML", *locator_cat)
            print(lst)
            lst = random.choice(lst)
            self.browser.send_keys_to_element(self.locator.CATEGORY, lst)
            self.browser.send_keys_to_element(
                self.locator.CATEGORY, Keys.ENTER)
            n -= 1

    def add_category(self, categories, *locator):
        """
        Method for add specific categories
        :param locator_cat: css selector or xpath
        :return:
        """
        elem = list(categories)
        lst = self.browser.get_list_element('innerHTML', *locator)
        count = len(elem)  # counter
        while count > 0:
            if elem[count - 1] in lst:
                self.browser.send_keys_to_element(
                    self.locator.CATEGORY, elem[count - 1])
                self.browser.send_keys_to_element(
                    self.locator.CATEGORY, Keys.ENTER)
                count -= 1
            else:
                return 'Error, Category {} not existed'.format(elem[count])

    def select_country(self, *locator):
        """
        Method for adding country (random)
        :param locator: css selector or xpath
        :return:
        """
        country = self.browser.select_from_list(self.locator.COUNTRY)
        confirm = self.browser.send_keys_to_element(*locator, country)
        return confirm

    def select_city(self, *locator):
        """
        Method for adding country (random)
        :param locator: css selector or xpath
        :return:
        """
        num = 3  # three attemp for choose city
        while num > 0:
            city = self.browser.select_from_list(self.locator.CITY)
            if len(city) > 0:
                confirm = self.browser.send_keys_to_element(*locator, city)
                return confirm
            else:
                num -= 1

    def press_button_save(self):
        self.browser.click_on_element(self.locator.SAVE)
