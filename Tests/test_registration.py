from Data.credentials import user, admin
import pytest
import allure
from Locators.locators import NavigationMenuLocators
from dbconnection import Connection
locator = NavigationMenuLocators

@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Register User')
@allure.story('User have ability to register in EventsExpress app')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("delete_registed_user")
def test_registration(app):
    app.auth.click_on_login_button()
    app.auth.click_register()
    app.auth.type_email_register("katya@gmail.com")
    app.auth.type_password_register("popalava09")
    app.auth.type_repassword_register("popalava09")
    db = Connection()
    db.confirm_useremail_on_register("katya@gmail.com")
    app.auth.click_on_login_button()
    app.auth.click_signin_tab()
    app.auth.clean_login_field()
    app.auth.type_login("katya@gmail.com")
    app.auth.clean_password_field()
    app.auth.type_pass("popalava09")
    app.auth.press_button_signin()
    assert app.base.check_if_element_exists(locator.PROFILE)
