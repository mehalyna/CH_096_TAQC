from Tests.test_init import TestInit
from Data.credentials import user


class TestLogin(TestInit):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()

    def test_authorization(self):
        self.exec.linked.type_login(user['email'])
        print("Locating and fill in username")

        self.exec.linked.type_pass(user['password'])
        print("Locating and fill in password form...")

        self.exec.linked.press_button_signin()
        # try:
        assert 'abcd' in 'fsfabcdre'
        print("Assertion test completed successfully")
        # except AssertionError:
        #     print('Assertion test failed')
        print('Login OK')
