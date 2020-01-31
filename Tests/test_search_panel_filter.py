# test Search event by date
import allure
import pytest


@allure.feature('Search field')
@allure.story("Search EVENT")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_admin", "create_event", "delete_event")
def test_search_event(app):
    """Chech if working search to filter. Search event by date."""
    app.search.open_filter()
    app.search.enter_date_from('02/8/20')
    app.search.enter_date_to('02/10/20')
    app.search.click_button_search()
    assert app.search.check_name_event() == "Test Event"
