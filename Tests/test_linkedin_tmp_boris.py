import pytest
import allure
from Data.credentials import user


# class TestLogin():
@allure.feature('Login page')
@allure.story('The first step')
def test_login(app, screenshot_on_failure):
    app.linked.type_login(user['email'])
    print("Locating and fill in username")

    app.linked.type_pass(user['password'])
    print("Locating and fill in password form...")

    app.linked.press_button_signin()

    # get title of the page
    expected_title = 'Security Verification'  # 'Fool'
    actual_title = app.linked.title
    print(f'It is expected a part of page title to be "{expected_title}".'
          f'The actual title is "{actual_title}"')

    # try:
    assert expected_title in actual_title
    print("Assertion test completed successfully")
    # except AssertionError:
    #     print('Assertion test failed')


if __name__ == '__main__':
    pytest.main()