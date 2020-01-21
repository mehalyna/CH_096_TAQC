"""Test possibility to communication user with admin"""
import allure
import pytest

from utilities.testLogging import PyLogging
from Locators.locators import ContactUsPageLocators as locator


@allure.feature("Positive test")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "http://34.65.101.58:5002/contactUs",
    name='"Contact us" page')
@allure.story('Test sending message to admin')
@allure.suite('Tests for "Contact us page"')
@pytest.mark.usefixtures("login", "screenshot_on_failure")
def test_contact_us(app):
    """A testcase to check user communication with admin"""
    loger = PyLogging(__name__)
    loger.info("New test:")
    message_error = "Test Failed, message don't send to admin"

    with allure.step("Checking username"):
        try:
            username = app.contact.check_username()
            if not username:
                loger.error("Username don't 'UserTest' ")
                assert username, "Username don't 'UserTest' "
            else:
                loger.info("Username is equal to 'UserTest'")
        except Exception:
            loger.exception("")
            assert username, "Username don't 'UserTest' "
    with allure.step("Go to 'Contact us' page."):
        try:
            app.navigation.click_on_contact_us()
            loger.info("Go to 'Contact us' page.")
        except Exception:
            loger.exception("")
            assert False, "Fail, can't go to the 'Contact us' page"
    with allure.step("Check if button 'Submit' isn't clickable"):
        try:
            app.base.element_be_clickable(locator.SUBMIT)
            loger.info("Check if button 'Submit' isn't clickable")
        except Exception:
            loger.exception("")
            assert False, "Button 'Submit' is clickable"
    with allure.step("Choose type from the list"):
        try:
            app.contact.check_type()
            loger.info("Choose type from the list")
        except Exception:
            loger.exception("")
            assert False, "Can't choose type"
    with allure.step("Enter description"):
        try:
            app.contact.enter_description()
            loger.info("Enter description")
        except Exception:
            loger.exception("")
            assert False, "Can't enter description"
    with allure.step("Click on 'Submit' button"):
        try:
            app.base.click_on_element(locator.SUBMIT)
            loger.info("Click on 'Submit' button")
        except Exception:
            loger.exception("")
            assert False, "Button 'Submit' isn't active"
    with allure.step("Test passed"):
        try:
            res = app.contact.get_text_from_result()
            if not res:
                loger.error(message_error)
                assert res, message_error
            else:
                loger.info("Test Passed")
        except Exception:
            loger.exception("")
            assert res, message_error
