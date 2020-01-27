import pytest
import allure
from Data.test_data import PROFILE_PAGE_EVENTS_MENU as Data



@allure.suite('Tests for "Events_menu page"')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("test_input", [Data.FUTURE_EVENTS,
                                        Data.ARCHIVE_EVENTS,
                                        Data.VISITED_EVENTS,
                                        Data.EVENTS_TO_GO,
                                        Data.ADD_EVENT])
@pytest.mark.usefixtures("login", "screenshot_on_failure")
def test_event_menu_existence(app, test_input):
    """
    Verify existence of each tab at the event menu panel
    :param app: - is a fixture of an instance of POM
    :param test_input: - parametrized names of each menu entry
    :return: assertion result
    """
    app.navigation.click_on_profile()
    assert app.event_menu.element_at_menu_bar_is_present(test_input, timeout=0),\
        f"No menu tab {test_input} in the tabs"
    print(f"Menu tab {test_input} is in the tab")


@allure.suite('Tests for "Events_menu page"')
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
    :param app: - is a fixture of an instance of POM
    :param menu_tab: - parametrized names of each menu entry
    :return: assertion result
    """
    app.navigation.click_on_profile()
    app.event_menu.click_menu_item(menu_tab)
    # Check item name by using the tab attribute aria-selected=true referred as 'ACTIVE TAB'
    # tab_name = app.event_menu.get_text_tab('ACTIVE TAB')
    tab_name = app.event_menu.get_text_tab('ACTIVE TAB')
    assert tab_name == menu_tab,\
        f"Wrong tab for {menu_tab} entry is active {tab_name}"
    print(f"Menu tab {menu_tab} is displayed as {tab_name}")


@allure.suite('Tests for "Events_menu page"')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("screenshot_on_failure", "login")
def test_count_tabs(app):
    """
    Counts a number of tabs at the menu panel
    :param app: - is a fixture of an instance of POM
    :return: assertion result
    """
    app.navigation.click_on_profile()
    tabs_count = app.event_menu.count_tabs("TABS_COUNT")
    expected_tabs_count = Data.TABS_QUANTITY
    assert tabs_count == expected_tabs_count,\
        f"Wrong quantity {tabs_count} of tabs displayed at the menu panel." \
        f" Only {expected_tabs_count} is expected."
