from Data.credentials import user


class TestLogin():

    def test_authorization(event):
        event.auth.click_on_login_button()
        event.auth.clean_login_field()
        event.auth.type_login( user['email'])
        event.auth.clean_password_field( )
        event.auth.type_pass(user['password'])
        event.auth.press_button_signin()
















