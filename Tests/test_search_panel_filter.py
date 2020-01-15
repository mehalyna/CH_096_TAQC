from Data.credentials import user,admin
import allure


@allure.feature('Search field')
@allure.story("Search EVENT")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_event(app):
    with allure.step('Login as admin'):
        app.signin.enter_actor( admin['email'], admin['password'] )
    with allure.step('Open filter form'):
        app.search.open_filter()
    with allure.step('Choose date'):
        app.search.enter_date_from('12/19/19')
        app.search.enter_date_to('12/20/19')
    with allure.step('Search event'):
        app.search.click_button_search()
    assert (app.search.check_name_event() == "test")
