import pytest
import allure
from Data.test_data import ProfilePageEventsMenu as Data
from Locators.locators import ProfilePageEventsMenuLocators as Tabs


@allure.suite('Tests for "Events_menu page"')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_input", [Data.FUTURE_EVENTS,
                                        Data.ARCHIVE_EVENTS,
                                        Data.VISITED_EVENTS,
                                        Data.EVENTS_TO_GO,
                                        Data.ADD_EVENT])
def test_event_menu_existence(app, login, screenshot_on_failure, test_input):
    app.navigation.click_on_profile()
    assert app.event_menu.element_at_menu_bar_is_present(test_input, timeout=0),\
        f"No menu tab {test_input} in the tabs"
    print(f"Menu tab {test_input} is in the tab")


# In progress... 2nd and consecutive tests are fail
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("menu_tab", [Data.FUTURE_EVENTS,
                                      Data.ARCHIVE_EVENTS,
                                      Data.VISITED_EVENTS,
                                      Data.EVENTS_TO_GO,
                                      Data.ADD_EVENT])
@pytest.mark.usefixtures("login", "screenshot_on_failure")
def test_event_menu_switch(app, menu_tab):
    """
    Moving from the first default tab to the next tabs and check \
    the result by selecting en element
    """
    app.navigation.click_on_profile()
    app.event_menu.click_menu_item(menu_tab)
    # Check item name by using the tab attribute aria-selected=true referred as 'ACTIVE TAB'
    # tab_name = app.event_menu.get_text_tab('ACTIVE TAB')
    tab_name = app.event_menu.get_text_tab()
    assert tab_name == menu_tab
    print(f"Menu tab {menu_tab} is displayed as {tab_name}")


# ToDo
# @allure.severity(allure.severity_level.CRITICAL)
# @pytest.mark.usefixtures("screenshot_on_failure")

# @pytest.mark.parametrize("item_name", ['TABS_COUNT'])
@pytest.mark.usefixtures("login")
def test_count_tabs(app):
    print(f'menu items = {"TABS_COUNT"}')
    variable = 0
    # Tabs.locators_dict['TABS']
    tabs_count = app.event_menu.count_tabs(Tabs.locators_dict['TABS'])
    print(f'menu items = {tabs_count}')

