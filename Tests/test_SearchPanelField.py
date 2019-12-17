from Tests.test_init import TestInit
from Data.credentials import user,admin





class TestSearchEvent(TestInit):

    def setUp(self):
        super().setUp()
        self.exec.signin.enter_actor(admin['email'],admin['password'])


    def test_search_event(self):
        self.exec.search.type_in_search_field('Python')
        self.exec.search.check_element()
        self.exec.search.click_button_search()
        self.assertEqual(self.exec.search.check_element(self.locator.FIELD_NAME_EVENT), "Python MeetUp")