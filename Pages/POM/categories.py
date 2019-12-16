from Locators.locators import CategoriesLocators
from Locators.locators import NavigationMenuLocators



class Categories():

    def __init__(self, browser):
        self.browser = browser
        self.locator_categories = CategoriesLocators
        self.locator_nav = NavigationMenuLocators


    def click_on_categories(self):
        self.browser.click_on_element(self.locator_nav.CATEGORIES)

    def add_category(self):
        self.browser.click_on_element(self.locator_categories.ADD_CATEGORY_BUTTON)
        self.browser.send_keys_to_element(self.locator_categories.ADD_CATEGORY_FIELD)
        self.browser.click_on_element(self.locator_categories.ADD_CATEGORY_CHECK)


    def click_on_search_user(self):
        

    def click_on_comuna(self):
        self.browser.click_on_element(self.locator.COMUNA)
