from Data.credentials import user,admin
import allure
import pytest



@allure.link("http://localhost:49862/home/events?page=1", name='Click me')
@allure.feature('Search Panel')
@allure.story('Search event')
@pytest.mark.usefixtures()
def test_search_event(app, screenshot_on_failure):
    app.signin.enter_actor( admin['email'], admin['password'] )
    app.search.open_filter()
    app.search.enter_date_from('12/19/19')
    app.search.enter_date_to('12/20/19')
    #self.exec.search.click_to_categories()
    app.search.click_button_search()
    assert (app.search.check_name_event() == "test")
 