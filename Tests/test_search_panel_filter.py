import pytest

from Data.credentials import user,admin
import allure


@allure.feature('Search field')
@allure.story("Search EVENT")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_admin")
def test_search_event(app):
    """Chech if working search to filter. Search event by date."""
    with allure.step('Open filter form'):
        app.search.open_filter()
    with allure.step('Choose date'):
        app.search.enter_date_from('12/19/19')
        app.search.enter_date_to('12/20/19')
    with allure.step('Search event'):
        app.search.click_button_search()
    assert (app.search.check_name_event() == "test")
