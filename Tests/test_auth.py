from Data.credentials import user,admin
import pytest
import allure
from Locators.locators import NavigationMenuLocators
from allure_commons.types import AttachmentType


locator = NavigationMenuLocators

def credentials():
    lst = [[user['email'],user['password']],[admin['email'],admin['password']]]
    return lst

@allure.feature('Login User')
@allure.story('"Actors" login to site EventExpress ')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('data',credentials())
def test_authorization(app,data):
    app.auth.click_on_login_button()
    app.auth.clean_login_field( )
    app.auth.type_login(data[0])
    app.auth.clean_password_field( )
    app.auth.type_pass(data[1])
    app.auth.press_button_signin( )
    try:
        assert app.base.click_to_element(locator.Home)
    except:
        allure.attach(app.base.screenshot_allure(), name='testLoginScreen',
                      attachment_type=AttachmentType.PNG)


















