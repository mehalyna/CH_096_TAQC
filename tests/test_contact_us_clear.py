"""
Test for checking if button 'Clear' working properly
"""
import allure
import pytest
from locators.locators import ContactUsPageLocators as locator


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
    message_error = "Test Failed: button 'Clear' isn't active"

    username = app.contact.check_username()
    assert username, "Username don't 'UserTest' "
    app.navigation.click_on_contact_us()
    app.base.element_be_clickable(locator.CLEAR)
    app.contact.check_type()
    app.contact.enter_description()
    app.base.click_on_element(locator.SUBMIT)
    res = app.contact.get_text_from_desc()
    assert res, message_error

