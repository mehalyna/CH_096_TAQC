"""
Test for checking if button 'Clear' working properly
"""
import allure
import pytest
from utilities.testLogging import PyLogging
from Locators.locators import ContactUsPageLocators as locator


@allure.suite('Tests for "Contact us page"')
@allure.feature("Check if button 'Clear' is active")
@allure.link(
    "http://34.65.101.58:5002/contactUs",
    name='"Contact us" page')
@allure.story("Test checking if button 'Clear' is active")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login", "screenshot_on_failure")
def test_contact_us_clear(app):
    """
    Check if the button 'Clear' working properly
    """
    loger = PyLogging(__name__)
    loger.info("New test:")
    message_error = "Test Failed: button 'Clear' isn't active"

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
    with allure.step("Check if button 'Clear' isn't clickable"):
        try:
            app.base.element_be_clickable(locator.CLEAR)
            loger.info("Check if button 'Clear' isn't clickable")
        except Exception:
            loger.exception("")
            assert False, "Button 'Clear' is clickable"
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
    with allure.step("Click on 'Clear' button"):
        try:
            app.base.click_on_element(locator.SUBMIT)
            loger.info("Click on 'Clear' button")
        except Exception:
            loger.exception("")
            assert False, "Button 'Clear' isn't active"
    with allure.step("Test passed"):
        try:
            res = app.contact.get_text_from_desc()
            if not res:
                loger.error(message_error)
                assert res, message_error
            else:
                loger.info("Test passed:button 'Clear' work correct")
        except Exception:
            loger.exception("")
            assert res, message_error
