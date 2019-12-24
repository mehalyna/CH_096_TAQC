import pytest
from Data.test_data import ProfileMenuPageHeaderInfo as data


@pytest.mark.parametrize("userinfo_input, userinfo_expected_value", [(data.USER_NAME_LABEL, data.USER_NAME_DATA),
                                                                     (data.USER_AGE_LABEL, data.USER_AGE_DATA),
                                                                     (data.USER_GENDER_LABEL, data.USER_GENDER_DATA),
                                                                     (data.USER_EMAIL_LABEL, data.USER_EMAIL_DATA),
                                                                     (data.USER_INTERESTS_LABEL, data.USER_INTERESTS_DATA)
                                                                     ])
def test_event_menu_existence(app, login, userinfo_input, userinfo_expected_value):
    actual_text = app.event_menu.get_text(userinfo_input, userinfo_expected_value)
    assert actual_text is  userinfo_expected_value,\
        f"Text of {userinfo_input} item differs. The expected one is {userinfo_expected_value} instead {actual_text} is displayed"
    print(f"Text of {userinfo_input} is in the tab {userinfo_expected_value}")