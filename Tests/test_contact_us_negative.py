"""
Test appearance message 'Required'
"""
import allure
import pytest
from utilities.testLogging import PyLogging
from Locators.locators import ContactUsPageLocators as locator


@allure.suite('Tests for "Contact us page"')
@allure.feature("Message 'Required'")
@allure.link(
    "http://34.65.101.58:5002/contactUs",
    name='"Contact us" page')
@allure.story("Test appearance message 'Required'")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login", "screenshot_on_failure")
def test_contact_us_negative(app):
    """
    Checking the required field "Description"
    """
    loger = PyLogging(__name__)
    loger.infos.append("New test:")
    message_error = "Test Failed, didn't show message 'Required'"

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
    with allure.step("Click on 'Submit' button"):
        try:
            app.base.click_on_element(locator.SUBMIT)
            loger.info("Click on 'Submit' button")
        except Exception:
            loger.exception("")
            assert False, "Button 'Submit' isn't active"
    with allure.step("Test passed:message 'Required' is present"):
        try:
            res = app.contact.get_text_from_mes()
            if not res:
                loger.info(message_error)
                assert res, message_error
            else:
                loger.info("Test Passed:message 'Required' is present")
        except Exception:
            loger.exception("")
            assert res, message_error

