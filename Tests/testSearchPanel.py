from Tests.test_main import TestInit
from Pages.LoginPage import LoginPage
from Data.TestData import TestData
from Pages.searchPanelPage import SearchPage


class TestSearch(TestInit):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()
        self.login = LoginPage(self.driver)
        self.login.login_user(TestData.LOGIN_USER, TestData.PASSWORD_USER)

    def test_search_to_date(self):
        self.search = SearchPage(self.driver)
        self.search.open_filter()
        self.search.enter_date_from('12/19/19')
        self.search.enter_date_to('12/20/19')
        self.search.click_button_search()

