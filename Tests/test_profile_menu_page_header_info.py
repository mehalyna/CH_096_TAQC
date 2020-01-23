import pytest
import allure
from Data.test_data import ProfileMenuPageHeaderInfo as Data
from Locators.locators import ProfileMenuPageHeaderInfoLocators as Locator


@allure.severity(allure.severity_level.TRIVIAL)
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
@pytest.mark.usefixtures("login")
def test_event_menu_header_info_text(app, userinfo_input):
    app.navigation.click_on_profile()
    actual_text = app.event_menu.get_text(userinfo_input)
    userinfo_expected_value = userinfo_input
    assert actual_text == userinfo_expected_value, f"Text of {userinfo_input} item differs."\
        f"The expected one is {userinfo_expected_value} instead {actual_text} is displayed"
    print(f"Text of {userinfo_input} is in the tab {userinfo_expected_value}")

#@pytest.mark.skip(reason='Postponed for USER_INTERESTS_DATA actualizing')

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('userinfo_input', list(Data.USER_INTERESTS_DATA))
def test_event_menu_header_info_text_interests(app, login, userinfo_input):
    """
    Check the Interests list
    ToDo
    >       return self.browser.get_element_text(self.locator_info[item_name])
    E       KeyError: <class 'Locators.locators.ProfileMenuPageHeaderInfoLocators'>

    ..\Pages\POM\event_menu_page.py:33: KeyError
    """
    app.navigation.click_on_profile()
    actual_text = app.event_menu.get_text(Locator)
    userinfo_expected_value = Data.USER_INTERESTS_DATA
    assert actual_text in userinfo_expected_value, f"Text of {userinfo_input} item differs. \
                            The expected one is {userinfo_expected_value}  \
                            instead {actual_text} is displayed"
    print(f"Text of {userinfo_input} is in the tab {userinfo_expected_value}")
