# test Search event by name
import allure
import pytest


@allure.feature('Search field')
@allure.story("Search EVENT")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_admin", "create_event", "delete_event")
def test_search_event(app):
    """Search event by name"""
    app.search.type_in_search_field('Test Event') 
    app.search.click_button_search()  
    assert app.search.check_name_event() == "Test Event"
