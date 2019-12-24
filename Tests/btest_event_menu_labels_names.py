import pytest
from Data.test_data import ProfilePageEventsMenu as data
    # CartPanelsAtProfilePage

# ToDo not ready
@pytest.mark.parametrize("test_input", [data.FUTURE_EVENTS,
                                        data.ARCHIVE_EVENTS,
                                        data.VISITED_EVENTS,
                                        data.EVENTS_TO_GO,
                                        data.ADD_EVENT])
def test_event_menu_existence(app, login, test_input):
    app.navigation.click_on_profile()
    assert app.event_menu.element_at_menu_bar_is_present(test_input, timeout=0), f"No menu tab {test_input} in the tabs"
    print(f"Menu tab {test_input} is in the tab")