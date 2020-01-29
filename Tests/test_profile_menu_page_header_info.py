"""
Test module for the header, displayed at profile page from navigation menu
"""
import pytest
import allure
from config import PROFILE_MENU_INFO as Data


@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.parametrize("userinfo_input", ['User Name:',
                                            'UserTest',
                                            'Age:',
                                            '35',
                                            'Gender:',
                                            'Female',
                                            'Email:',
                                            'user@gmail.com',
                                            'Interests:'
                                            ])
@pytest.mark.usefixtures("login")
def test_event_menu_header_info_text(app, userinfo_input):
    """
    A test for menu header text info.
    :param app: instance of a page object, passed here as fixture
    :param userinfo_input: parametrized test data as fixture
    :return: assertion result
    """
    app.navigation.click_on_profile()
    actual_text = app.event_menu.get_text(userinfo_input)
    userinfo_expected_value = userinfo_input

    assert actual_text == userinfo_expected_value, \
        f"Text of {userinfo_input} item differs."\
        f"The expected one is {userinfo_expected_value} instead {actual_text} is displayed"

    print(f"Text of {userinfo_input} is in the tab {userinfo_expected_value}")

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login")
def test_event_menu_header_info_text_interests(app):
    """
    Check the Interests list
    """
    app.navigation.click_on_profile()
    actual_text = app.event_menu.get_text('USER_INTERESTS_DATA').replace('#', '').split('\n')
    userinfo_expected_value = list(Data['User_interests_data'])

    assert sorted(actual_text) == sorted(userinfo_expected_value), \
        f"Text of {sorted(actual_text)} item differs." \
        f"The expected one is {sorted(userinfo_expected_value)}" \
        f"instead {actual_text} is displayed"

    print(f"Text of {sorted(actual_text)} is in the tab vs expected {sorted(userinfo_expected_value)}")
