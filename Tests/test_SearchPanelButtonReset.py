from Tests.test_init import TestInit
from Data.credentials import user,admin
from Locators.locators import SearchEventPanelLocators





class TestSearchEvent(TestInit):
    def __init__(self):
        self.locator = SearchEventPanelLocators

    def setUp(self):
        super().setUp()
        self.exec.signin.enter_actor(admin['email'],admin['password'])


    def test_search_event(self):
        self.exec.search.type_in_search_field('Python MeetUp')
        self.exec.search.click_button_search()
        self.assertEqual(self.exec.search.check_element(), "Python MeetUp")