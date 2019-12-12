from Tests.test_main import TestLoginToSite
from Pages.LoginPage import LoginPage
from Data.TestData import TestData


class Test_Login(TestLoginToSite):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()



    def test_login_if_user_entered(self):
        self.login_Page = LoginPage( self.driver )
        self.login_Page.click_on_login_button()
        self.login_Page.type_login(TestData.LOGIN_USER)
        self.login_Page.type_pass(TestData.PASSWORD_USER)
        self.login_Page.press_button_signin()