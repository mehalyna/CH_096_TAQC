"""Test auth"""
import pytest
import allure
from config import CREDENTIALS
from Locators.locators import NavigationMenuLocators


locator = NavigationMenuLocators


def credentials():
    """credentials"""
    lst = [[CREDENTIALS['User_name'], CREDENTIALS['User_password']],
           [CREDENTIALS['Admin_name'], CREDENTIALS['Admin_password']]]
    return lst


@allure.link("http://localhost:50621/home/events?page=1", name='Click me')
@allure.feature('Login User')
@allure.story('"Actors" login to site EventExpress ')
@pytest.mark.parametrize('data',credentials())
@allure.severity(allure.severity_level.CRITICAL)
def test_authorization(app, data):
    """Test auth"""
    app.auth.click_on_login_button()
    app.auth.clean_login_field()
    app.auth.type_login(data[0])
    app.auth.clean_password_field()
    app.auth.type_pass(data[1])
    app.auth.press_button_signin()
    assert app.base.check_if_element_exists(locator.PROFILE)
