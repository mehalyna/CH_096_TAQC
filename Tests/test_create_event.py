from Tests.test_init import TestInit
from Data.credentials import user,admin




class TestCreateEvent(TestInit):

    def setUp(self):
        super().setUp()




    def test_create_event(self):
        self.exec.signin.enter_actor(user['email'],user['password'])
        self.exec.navigation.click_on_profile()
        self.exec.prof_menu.click_on_add_event()






