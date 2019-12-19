<<<<<<< HEAD
=======
from Tests.testinit import TestInit
>>>>>>> pytest start
from Data.credentials import user,admin
import allure
from selenium.common.exceptions import NoSuchElementException
from allure_commons.types import AttachmentType
from Locators.locators import SearchEventPanelLocators as locator



@allure.feature('Search field')
@allure.story("Search EVENT")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_event(app):
    with allure.step('Login as admin'):
        app.signin.enter_actor(admin['email'],admin['password'])
    with allure.step('Search event'):
        app.search.type_in_search_field('Python MeetUp')
        app.search.click_button_search()
    try:
        assert app.base.check_if_element_exists( locator.FIELD_NAME_EVENT )
    except:
        with allure.step('Take Screenshot'):
            allure.attach( app.base.screenshot_allure( ), name='testScreenLogin',
                       attachment_type=AttachmentType.PNG )
        raise NoSuchElementException
        
