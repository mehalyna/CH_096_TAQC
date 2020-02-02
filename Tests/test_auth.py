"""Test auth"""

import pytest
import allure
from config import CREDENTIALS
from locators.locators import HomePageLocators


locator = HomePageLocators


def credentials():
    """credentials"""
    lst = [[CREDENTIALS['User_name'], CREDENTIALS['User_password']],
           [CREDENTIALS['Admin_name'], CREDENTIALS['Admin_password']]]
    return lst


@allure.link("http://localhost:50621/home/events?page=1", name='Click me')
@allure.feature('Actors login')
@allure.story('"Actors" can perform login to site EventExpress ')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("name, password, username", [('user@gmail.com', '1qaz1qaz', 'UserTest'),
                                                      ('admin@gmail.com', '1qaz1qaz', 'Admin')])
def test_authorization(app, name, password, username):
    """
    Test for authorization
    """
    app.auth.fill_login_data(name, password)
    assert app.base.get_element_text(locator.NAME_USER) == username
