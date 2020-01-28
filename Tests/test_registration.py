import pytest
import allure
from Locators.locators import NavigationMenuLocators
from dbconnection import Connection
locator = NavigationMenuLocators
from config import INFO_REGISTRATION as info



@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Register User')
@allure.story('User have ability to register in EventsExpress app')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("delete_registered_user")
def test_registration(app):
    with allure.step("fill register form"):
        app.auth.fill_register_data(info['email_for_register'], info['password_for_register'])
        app.auth.send_escape()
    with allure.step("Confirm a user"):
        db = Connection()
        db.confirm_useremail_on_register(info['email_for_register'])
    with allure.step("fill login form"):
        app.auth.fill_login_data(info['email_for_register'], info['password_for_register'])
    with allure.step("Verify successfully login"):
        assert app.base.check_if_element_exists(locator.PROFILE)


@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Register User')
@allure.story('User does not have an ability to register with already existing email')
@allure.severity(allure.severity_level.NORMAL)
def test_registration_existing_email(app):
    with allure.step("fill register form"):
        app.auth.fill_register_data(info['existing_mail'], info['password_for_register'])
    with allure.step("Verify that warning message appears"):
        assert app.auth.check_warning_message_about_existing_email() == info['warning_message_about_exists_email']


@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Register User')
@allure.story('User does not have an ability to register with invalid email filled')
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_invalid_email(app):
    with allure.step("fill register form"):
        app.auth.fill_register_data(info['invalid_mail'], info['password_for_register'])
    with allure.step("Verify that warning message about invalid email appears"):
        assert app.auth.check_warning_message_about_invalid_email() == info['warning_message_about_invalid_mail']


@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Register User')
@allure.story('User does not have an ability to register with invalid password')
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_invalid_password(app):
    with allure.step("fill register form"):
        app.auth.fill_register_data(info['mail_for_invalid_pass'], info['invalid_pass'])
    with allure.step("Verify that warning message about invalid password appears"):
        assert app.auth.check_warning_message_about_invalid_password() == info['warning_message_about_invalid_pass']
