# test Search event by name
import allure
import pytest

from Data.credentials import admin


@allure.feature('Search field')
@allure.story("Search EVENT")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_admin")
def test_search_event(app):
    """Search event by name"""
    with allure.step('Search event'):
        app.search.type_in_search_field('Python MeetUp')
        app.search.click_button_search()
