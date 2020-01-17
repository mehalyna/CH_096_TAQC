import pytest
import allure
from Data.test_data import ProfilePageEventsMenu as Data


@allure.suite('Tests for "Events_menu page"')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_input", [Data.FUTURE_EVENTS,
                                        Data.ARCHIVE_EVENTS,
                                        Data.VISITED_EVENTS,
                                        Data.EVENTS_TO_GO,
                                        Data.ADD_EVENT])
def test_event_menu_existence(app, login, screenshot_on_failure, test_input):
    app.navigation.click_on_profile()
    assert app.event_menu.element_at_menu_bar_is_present(test_input, timeout=0), f"No menu tab {test_input} in the tabs"
    print(f"Menu tab {test_input} is in the tab")


# In progress... bj 2nd and consecutive tests are fail
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("menu_tab", [Data.FUTURE_EVENTS,
                                      Data.ARCHIVE_EVENTS,
                                      Data.VISITED_EVENTS,
                                      Data.EVENTS_TO_GO,
                                      Data.ADD_EVENT])
def test_event_menu_switch(app, login, screenshot_on_failure, menu_tab):
    """ Moving from default the first tab to the next tab and check the result by locating
    corresponding tab indicator"""
    app.navigation.click_on_profile()
    app.event_menu.click_menu_item(menu_tab)
    actual_result = app.event_menu.is_menu_item_active(menu_tab)
    assert actual_result
    print(f"Menu tab {menu_tab}")


# ToDo
# @allure.severity(allure.severity_level.CRITICAL)
# def test_count_events_menu_buttons(self, container, item_name):
#     lst = self.exec.event_menu.count_event_menu_entries(container, item_name)
#     print(f'menu items = {len(lst)}')
#     pass
