"""
Test appearance message 'Required'
"""
import allure
import pytest
from locators.locators import ContactUsPageLocators as locator


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
    message_error = "Test Failed, didn't show message 'Required'"

    username = app.contact.check_username()
    assert username, "Username don't 'UserTest' "
    app.navigation.click_on_contact_us()
    app.base.element_be_clickable(locator.SUBMIT)
    app.contact.check_type()
    app.base.click_on_element(locator.SUBMIT)
    res = app.contact.get_text_from_mes()
    assert res, message_error

