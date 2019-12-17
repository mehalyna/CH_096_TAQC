from Tests.test_init import TestInit
from Data.credentials import user,admin
from Data.test_data import CreateEventData
from Locators.locators import CreateEvent






class TestCreateEvent(TestInit):

    def setUp(self):
        super().setUp()
        self.event = CreateEventData
        self.locator = CreateEvent



    def test_create_event(self):
        self.exec.signin.enter_actor(user['email'],user['password'])
        self.exec.navigation.click_on_profile()
        self.exec.prof_menu.click_on_add_event()
        self.exec.creat_event.upload_image()
        self.exec.creat_event.add_title(self.event.TITLE)
        self.exec.creat_event.add_desc(self.event.DESCRIPTION['New Year'])







