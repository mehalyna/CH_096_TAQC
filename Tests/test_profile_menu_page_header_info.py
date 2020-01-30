"""
Test module for the header, displayed at profile page from navigation menu
"""
import pytest
import allure
# from data.test_data import PROFILE_MENU_INFO as data
from config import PROFILE_MENU_INFO as Data
# from locators.locators import ProfileMenuPageHeaderInfoLocators as Locator
from locators.locators import ProfileMenuPageHeaderInfoLocators as Locator


@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.parametrize("userinfo_input", ['User Name:',
                                            'UserTest',
                                            'Age:',
                                            '35',
                                            'Gender:',
                                            'Other',
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
    assert actual_text == userinfo_expected_value, f"Text of {userinfo_input} item differs."\
        f"The expected one is {userinfo_expected_value} instead {actual_text} is displayed"
    print(f"Text of {userinfo_input} is in the tab {userinfo_expected_value}")


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('userinfo_input', list(Data['User_interests_data']))
@pytest.mark.usefixtures("login")
def test_event_menu_header_info_text_interests(app, userinfo_input):
    """
    Check the Interests list
    """
    app.navigation.click_on_profile()
    actual_text = app.event_menu.get_text(Locator)
    userinfo_expected_value = Data['User_interests_data']
    assert actual_text in userinfo_expected_value, f"Text of {userinfo_input} item differs. \
                            The expected one is {userinfo_expected_value}  \
                            instead {actual_text} is displayed"
    print(f"Text of {userinfo_input} is in the tab {userinfo_expected_value}")
