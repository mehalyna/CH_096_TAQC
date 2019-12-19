from Tests.testinit import TestInit
from Data.credentials import user,admin





class TestSearchEvent(TestInit):

    def setUp(self):
        super().setUp()
        self.exec.signin.enter_actor(user['email'],user['password'])


    def test_search_event(self):
        self.exec.search.open_filter()
        self.exec.search.enter_date_from('12/19/19')
        self.exec.search.enter_date_to('12/20/19')
        self.exec.search.click_button_search()
        self.assertEqual(self.exec.search.check_element(), "test")
