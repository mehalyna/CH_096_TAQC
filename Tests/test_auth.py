from Data.credentials import user,admin
import pytest
import allure
from Locators.locators import NavigationMenuLocators
from utilities.testLogging import PyLogging


locator = NavigationMenuLocators

def credentials():
    lst = [[user['email'],user['password']],[admin['email'],admin['password']]]
    return lst


@allure.link("http://localhost:50621/home/events?page=1", name='Click me')
@allure.feature('Login User')
@allure.story('"Actors" login to site EventExpress ')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('data',credentials())
def test_authorization(app, data, screenshot_on_failure):
    loger = PyLogging(__name__)
    loger.infos.append("New test:")
    messages = ("Click on login button",
                "Clean login field",
                "Enter login into field",
                "Clean password field",
                "Enter password into field",
                "Click on 'Signin' button"
                "Test Passed")
    messages_error = "Test Failed: we didn't login into application"
    with allure.step(messages[0]):
        app.auth.click_on_login_button()
        loger.info(messages[0])
    with allure.step(messages[1]):
        app.auth.clean_login_field( )
        loger.info(messages[1])
    with allure.step(messages[2]):
        app.auth.type_login(data[0])
        loger.info(messages[2])
    with allure.step(messages[3]):
        app.auth.clean_password_field( )
        loger.info(messages[3])
    with allure.step(messages[4]):
        app.auth.type_pass(data[1])
        loger.info(messages[4])
    with allure.step(messages[5]):
        app.auth.press_button_signin()
        loger.info(messages[5])
    res = app.base.check_if_element_exists( locator.PROFILE )
    if res == False:
        loger.error(messages_error)
        assert res, messages_error
    else:
        loger.info(messages[6])