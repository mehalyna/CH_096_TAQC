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
    with allure.step("Open login form"):
        app.auth.click_on_login_button()
    with allure.step("Open register tab"):
        app.auth.click_register()
    with allure.step("Fill data"):
        app.auth.type_email_register("katya@gmail.com")
        app.auth.type_password_register("popalava09")
        app.auth.type_repassword_register("popalava09")
        app.auth.send_escape()
    with allure.step("Confirm a user"):
        db = Connection()
        db.confirm_useremail_on_register("katya@gmail.com")
    with allure.step("Open login form"):
        app.auth.click_on_login_button()
        app.auth.click_signin_tab()
        app.auth.clean_login_field()
        app.auth.type_login("katya@gmail.com")
        app.auth.clean_password_field()
        app.auth.type_pass("popalava09")
        app.auth.press_button_signin()
    with allure.step("Verify successfully login"):
        assert app.base.check_if_element_exists(locator.PROFILE)


@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Register User')
@allure.story('User does not have an ability to register with already existing email')
@allure.severity(allure.severity_level.NORMAL)
def test_registration_existing_email(app):
    with allure.step("Open login form"):
        app.auth.click_on_login_button()
    with allure.step("Open register tab"):
        app.auth.click_register()
    with allure.step("Fill data"):
        app.auth.type_email_register("user@gmail.com")
        app.auth.type_password_register("popalava09")
        app.auth.type_repassword_register("popalava09")
    with allure.step("Verify that warning message appears"):
        assert app.auth.check_warning_message_about_existing_email() == "Email already exists in database"


@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Register User')
@allure.story('User does not have an ability to register with invalid email filled')
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_invalid_email(app):
    with allure.step("Open login form"):
        app.auth.click_on_login_button()
    with allure.step("Open register tab"):
        app.auth.click_register()
    with allure.step("Fill data"):
        app.auth.type_email_register("usergmail.com")
        app.auth.type_password_register("popalava09")
        app.auth.type_repassword_register("popalava09")
    with allure.step("Verify that warning message about invalid email appears"):
        assert app.auth.check_warning_message_about_invalid_email() == "Invalid email address"
