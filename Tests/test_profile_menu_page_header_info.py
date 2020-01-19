#!/usr/bin/python3

"""
Test module for the header, displayed at profile page from navigation menu
"""
import pytest
import allure
from Data.test_data import ProfileMenuPageHeaderInfo as Data
from Locators.locators import ProfileMenuPageHeaderInfoLocators as Locator


@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.usefixtures('login')
@pytest.mark.parametrize("userinfo_input", ['User Name:',
                                            'UserTest',
                                            'Age:',
                                            '19',
                                            'Gender:',
                                            'Other',
                                            'Email:',
                                            'user@gmail.com',
                                            'Interests:'
                                           ])
def test_header_info_text(app, userinfo_input):
    """
    A test for menu header text info.
    :param app: instance of a page object, passed here as fixture
    :param userinfo_input: parametrized test data as fixture
    :return: assertion result
    """
    app.navigation.click_on_profile()
    actual_text = app.event_menu.get_text(userinfo_input)
    userinfo_expected_value = userinfo_input
    warning = "Text of {} item differs. The expected one is {} instead {} is displayed"\
        .format(userinfo_input, userinfo_expected_value, actual_text)
    assert actual_text == userinfo_expected_value, warning
    print("Text of {} is in the tab {}".format(userinfo_input, userinfo_expected_value))


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures('login')
@pytest.mark.skip(reason='Postponed for USER_INTERESTS_DATA actualizing')
@pytest.mark.smoke
def test_header_interests(app, userinfo_input=Data.USER_INTERESTS_DATA):
    """Check the Interests list"""
    app.navigation.click_on_profile()
    actual_text = app.event_menu.get_text(Locator)
    userinfo_expected_value = Data.USER_INTERESTS_DATA
    warning = "Text of {} item differs. The expected one is {} instead {} is displayed".\
        format(userinfo_input, userinfo_expected_value, actual_text)
    assert actual_text in userinfo_expected_value, warning
    print("Text of {} is in the tab {}".format(userinfo_input, userinfo_expected_value))
    # print(f"Text of {userinfo_input} is in the tab {userinfo_expected_value}")
