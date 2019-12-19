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
<<<<<<< HEAD
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
    '''ToDo Uncertain condition for panels comparison.'''

    def setUp(self):
        super().setUp()
        self.timeout = 5

    def test_event_menu_switch_1(self, name='FUTURE EVENTS'):
        ''' Moving from default tab to FUTURE EVENTS and check '''
        self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
                                     CreateEventData.PASSWORD_USER)
        self.exec.navigation.click_on_profile()
        self.exec.event_menu.click_menu_item(name)  # 'FUTURE EVENTS'
        name = 'CART_PANEL'  # Condition of successful switch for empty panel
        self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
        print(f"Menu tab {name}")

    def test_event_menu_switch_2(self, name='ARCHIVE EVENTS'):
        ''' Moving from default tab to FUTURE EVENTS and check '''
        self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
                                     CreateEventData.PASSWORD_USER)
        self.exec.navigation.click_on_profile()
        self.exec.event_menu.click_menu_item(name)  # 'FUTURE EVENTS'
        name = 'CART_NTH'  # Condition of successful switch for non-empty panel
        self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
        print(f"Menu tab {name}")

    def test_event_menu_switch_3(self, name='VISITED EVENTS'):
        ''' Moving from "FUTURE EVENTS" tab to "VISITED EVENTS" and check '''
        self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
                                     CreateEventData.PASSWORD_USER)
        self.exec.navigation.click_on_profile()
        self.exec.event_menu.click_menu_item(name)  # VISITED EVENTS
        name = 'CART_PANEL'  # Condition of successful switch for non-empty panel
        self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
        print(f"Menu tab {name}")

    def test_event_menu_switch_4(self, name='EVENTS TO GO'):
        ''' Moving from "VISITED EVENTS" tab to "EVENTS TO GO" and check '''
        self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
                                     CreateEventData.PASSWORD_USER)
        self.exec.navigation.click_on_profile()
        self.exec.event_menu.click_menu_item(name)  # EVENTS TO GO
        name = 'CART_PANEL'  # Condition of successful switch for non-empty panel
        self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
        print(f"Menu tab {name}")
    #
    def test_event_menu_switch_5(self, name='ADD_EVENT'):
        ''' Moving from "EVENTS TO GO" tab to "ADD_EVENT" and check '''
        self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
                                     CreateEventData.PASSWORD_USER)
        self.exec.navigation.click_on_profile()
        self.exec.event_menu.click_menu_item(name)  # EVENTS TO GO
        name = 'ADD_EVENT_CART_CLEAR_BUTTON'  # Condition of successful switch for non-empty panel
        self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
        print(f"Menu tab {name}")
=======

#     def test_event_menu_2(self, name='ARCHIVE EVENTS'):
#         self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
#                                      CreateEventData.PASSWORD_USER)
#         self.exec.navigation.click_on_profile()
#         self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
#         print(f"Menu tab {name} is in the tab")
#
#
#     def test_event_menu_3(self, name='VISITED EVENTS'):
#         self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
#                                      CreateEventData.PASSWORD_USER)
#         self.exec.navigation.click_on_profile()
#         self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
#         print(f"Menu tab {name} is in the tab")
#
#
#     def test_event_menu_4(self, name='EVENTS TO GO'):
#         self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
#                                      CreateEventData.PASSWORD_USER)
#         self.exec.navigation.click_on_profile()
#         self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
#         print(f"Menu tab {name} is in the tab")
#
#
#     def test_event_menu_5(self, name='ADD_EVENT'):
#         self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
#                                      CreateEventData.PASSWORD_USER)
#         self.exec.navigation.click_on_profile()
#         self.assertTrue(self.exec.event_menu.element_at_menu_bar_is_present(name, self.timeout))
#         print(f"Menu tab {name} is in the tab")
#
#
# class TestEventMenuTabsSwitch(TestInit):
#     '''ToDo Uncertain conditions for panels comparison.'''
#
#     def setUp(self):
#         super().setUp()
#         self.timeout = 5
#
#     def test_event_menu_switch_1(self, name='FUTURE EVENTS'):
#         ''' Moving from default tab to FUTURE EVENTS and check '''
#         self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
#                                      CreateEventData.PASSWORD_USER)
#         self.exec.navigation.click_on_profile()
#         self.exec.event_menu.click_menu_item(name)  # 'FUTURE EVENTS'
#         name = 'CART_PANEL'  # Condition of successful switch for empty panel
#         self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
#         print(f"Menu tab {name}")
#
#     def test_event_menu_switch_2(self, name='ARCHIVE EVENTS'):
#         ''' Moving from default tab to FUTURE EVENTS and check '''
#         self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
#                                      CreateEventData.PASSWORD_USER)
#         self.exec.navigation.click_on_profile()
#         self.exec.event_menu.click_menu_item(name)  # 'FUTURE EVENTS'
#         name = 'CART_NTH'  # Condition of successful switch for non-empty panel
#         self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
#         print(f"Menu tab {name}")
#
#     def test_event_menu_switch_3(self, name='VISITED EVENTS'):
#         ''' Moving from "FUTURE EVENTS" tab to "VISITED EVENTS" and check '''
#         self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
#                                      CreateEventData.PASSWORD_USER)
#         self.exec.navigation.click_on_profile()
#         self.exec.event_menu.click_menu_item(name)  # VISITED EVENTS
#         name = 'CART_PANEL'  # Condition of successful switch for non-empty panel
#         self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
#         print(f"Menu tab {name}")
#
#     def test_event_menu_switch_4(self, name='EVENTS TO GO'):
#         ''' Moving from "VISITED EVENTS" tab to "EVENTS TO GO" and check '''
#         self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
#                                      CreateEventData.PASSWORD_USER)
#         self.exec.navigation.click_on_profile()
#         self.exec.event_menu.click_menu_item(name)  # EVENTS TO GO
#         name = 'CART_PANEL'  # Condition of successful switch for non-empty panel
#         self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
#         print(f"Menu tab {name}")
#
#     def test_event_menu_switch_5(self, name='ADD_EVENT'):
#         ''' Moving from "EVENTS TO GO" tab to "ADD_EVENT" and check '''
#         self.exec.signin.enter_actor(CreateEventData.LOGIN_USER,
#                                      CreateEventData.PASSWORD_USER)
#         self.exec.navigation.click_on_profile()
#         self.exec.event_menu.click_menu_item(name)  # EVENTS TO GO
#         name = 'ADD_EVENT_CART_CLEAR_BUTTON'  # Condition of successful switch for non-empty panel
#         self.assertTrue(self.exec.event_carts.element_at_menu_bar_is_present(name, self.timeout))
#         print(f"Menu tab {name}")
>>>>>>> Unittest before move into PyTest


        # self.exec.event_menu.click_menu_item(name)
        # self.exec.prof_menu.click_on_add_event()


    # def test_count_events_menu_buttons(self, container, item_name):
        # lst = self.exec.event_menu.count_event_menu_entries(container, item_name)
        # print(f'menu items = {len(lst)}')
        # pass
