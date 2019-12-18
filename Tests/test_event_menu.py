from Tests.test_init import TestInit
from Data.test_data import CreateEventData, CartPanelsAtProfilePage


class TestEventMenuTabsCheck(TestInit):

    def setUp(self):
        super().setUp()
        self.timeout = 0

    def test_event_menu_1(self, name='FUTURE EVENTS'):
        self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
                                     CreateEventData.PASSWORD_USER)
        self.exec.navigation.click_on_profile()
        self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
        print(f"Menu tab {name} is in the tab")
    #
    # def test_event_menu_2(self, name='ARCHIVE EVENTS'):
    #     self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
    #                                  CreateEventData.PASSWORD_USER)
    #     self.exec.navigation.click_on_profile()
    #     self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
    #     print(f"Menu tab {name} is in the tab")
    #
    #
    # def test_event_menu_3(self, name='VISITED EVENTS'):
    #     self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
    #                                  CreateEventData.PASSWORD_USER)
    #     self.exec.navigation.click_on_profile()
    #     self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
    #     print(f"Menu tab {name} is in the tab")
    #
    #
    # def test_event_menu_4(self, name='EVENTS TO GO'):
    #     self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
    #                                  CreateEventData.PASSWORD_USER)
    #     self.exec.navigation.click_on_profile()
    #     self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
    #     print(f"Menu tab {name} is in the tab")
    #
    #
    # def test_event_menu_5(self, name='ADD_EVENT'):
    #     self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
    #                                  CreateEventData.PASSWORD_USER)
    #     self.exec.navigation.click_on_profile()
    #     self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
    #     print(f"Menu tab {name} is in the tab")


class TestEventMenuTabsSwitch(TestInit):

    def setUp(self):
        super().setUp()
        self.timeout = 5

    def test_event_menu_switch(self, name='FUTURE EVENTS'):
        self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
                                     CreateEventData.PASSWORD_USER)
        self.exec.navigation.click_on_profile()
        self.exec.event_menu.click_menu_item(name)

        name = 'CART_PANEL'
        self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
        print(f"Menu tab {name} is in the tab")
    #
    # def test_event_menu_2(self, name='ARCHIVE EVENTS'):
    #     self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
    #                                  CreateEventData.PASSWORD_USER)
    #     self.exec.navigation.click_on_profile()
    #     self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
    #     print(f"Menu tab {name} is in the tab")
    #
    # def test_event_menu_3(self, name='VISITED EVENTS'):
    #     self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
    #                                  CreateEventData.PASSWORD_USER)
    #     self.exec.navigation.click_on_profile()
    #     self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
    #     print(f"Menu tab {name} is in the tab")
    #
    # def test_event_menu_4(self, name='EVENTS TO GO'):
    #     self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
    #                                  CreateEventData.PASSWORD_USER)
    #     self.exec.navigation.click_on_profile()
    #     self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
    #     print(f"Menu tab {name} is in the tab")
    #
    # def test_event_menu_5(self, name='ADD_EVENT'):
    #     self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
    #                                  CreateEventData.PASSWORD_USER)
    #     self.exec.navigation.click_on_profile()
    #     self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
    #     print(f"Menu tab {name} is in the tab")

        # self.exec.event_menu.click_menu_item(name)
        # self.exec.prof_menu.click_on_add_event()

    # def test_change_event_menu(self, from_tab, to_tab):
    #     pass
        # self.exec.search.type_in_search_field('Python')
        # self.exec.search.check_element()
        # self.exec.search.click_button_search()
        # self.assertEqual(self.exec.search.check_element(), "Python MeetUp")

    # def test_count_events_menu_buttons(self, container, item_name):
        # lst = self.exec.event_menu.count_event_menu_entries(container, item_name)
        # print(f'menu items = {len(lst)}')
        # pass
