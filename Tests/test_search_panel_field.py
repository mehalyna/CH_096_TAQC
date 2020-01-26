# test Search event by name
import allure
import pytest
from utilities.testLogging import PyLogging


@allure.feature('Search field')
@allure.story("Search EVENT")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_admin")
def test_search_event(app):
    """Search event by name"""
    worning_massage = "Essert error. Event not found"
    loger = PyLogging(__name__)
    loger.info("New test:")
    with allure.step('Search event'):
        try:
            loger.info('Type text in search field')
            app.search.type_in_search_field('Python MeetUp')    #test
            app.search.click_button_search()    #test
        except Exception:
            loger.exception("")
            assert False, "Fail"
    with allure.step('Event not found'):
        try:
            if (app.search.check_name_event() == "Python MeetUp"):  #test
                test_result = True
                loger.info("Done!")
            else:
                test_result = False
                assert test_result, "Event not found"
        except Exception:
            loger.error(worning_massage)
            loger.exception(worning_massage)
            assert False, worning_massage

    
