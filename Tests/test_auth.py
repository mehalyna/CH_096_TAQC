<<<<<<< HEAD
from Data.credentials import user,admin
import pytest
import allure
from Locators.locators import NavigationMenuLocators as locator


def credentials():
    lst = [[user['email'],user['password']],[admin['email'],admin['password']]]
    return lst


@allure.link("http://localhost:49862/home/events?page=1", name='Click me')
@allure.feature('Login User')
@allure.story('"Actors" login to site EventExpress ')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('data',credentials())
def test_authorization(app, data, screenshot_on_failure):
    app.auth.click_on_login_button()
    app.auth.clean_login_field()
    app.auth.type_login(data[0])
    app.auth.clean_password_field( )
    app.auth.type_pass(data[1])
    app.auth.press_button_signin()
    assert app.base.check_if_element_exists(locator.PROFILE)
=======
from Tests.testinit import TestInit

from Data.credentials import user



class TestLogin(TestInit):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()



    def test_authorization(self):
        self.exec.auth.click_on_login_button()
        self.exec.auth.clean_login_field()
        self.exec.auth.type_login( user['email'])
        self.exec.auth.clean_password_field( )
        self.exec.auth.type_pass(user['password'])
        self.exec.auth.press_button_signin()
















>>>>>>> pytest start
