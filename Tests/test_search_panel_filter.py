# test Search event by name
import allure
import pytest
from utilities.testLogging import PyLogging


@allure.feature('Search field')
@allure.story("Search EVENT")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_admin")
def test_search_event(app):
    """Chech if working search to filter. Search event by date."""
    worning_massage = "Essert error. Event not found"
    loger = PyLogging(__name__)
    loger.info("New test:")
    with allure.step('Open filter form'):
        try:
            loger.info('Open filter form')
            app.search.open_filter()    #test
        except Exception:
            loger.exception("Filter form don`t opened")
            assert False, "Filter form don`t opened"
    with allure.step('Choose date'):
        try:
            loger.info('Choose date')
            app.search.enter_date_from('01/21/20')  #test
            app.search.enter_date_to('02/20/20')    #test
        except Exception:
            loger.exception("Date don`t choosed")
            assert False, "Date don`t choosed"
    with allure.step('Search event'):
        try:
            loger.info('Search event')
            app.search.click_button_search()    #test
        except Exception:
            loger.exception("Event don`t searched")
            assert False, "Event don`t searched"
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
