from Tests.conftest import TestInit
from Data.credentials import user, admin


class TestCreateEvent(TestInit):

    def setUp(self):
        super().setUp()
        self.exec.signin.enter_actor(user['email'], user['password'])
        self.exec.navigation.click_on_profile()


    def test_event_menu(self):
        self.exec.event_menu.click_menu_item('ARCHIVE EVENTS')
        # self.exec.prof_menu.click_on_add_event()

    def test_count_events_menu_buttons(self, container, item_name):
        lst = self.exec.event_menu.count_event_menu_entries(container, item_name)
        print(f'menu items = {len(lst)}')
