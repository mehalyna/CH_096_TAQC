from Data.credentials import user,admin
import allure


@allure.feature('Search field')
@allure.story("Search event")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_event(app):
    with allure.step('Login as admin'):
        app.signin.enter_actor(admin['email'],admin['password'])
    with allure.step('Search event'):
        app.search.type_in_search_field('Python MeetUp')
        app.search.click_button_search()
        
