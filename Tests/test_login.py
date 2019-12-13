from Tests.test_main import TestLoginToSite
from Pages.LoginPage import LoginPage
from Data.TestData import TestData
 

class TestLogin(TestLoginToSite):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()


    def test_login_if_user_entered(self):
        self.login_Page = LoginPage( self.driver )
        self.login_Page.login_user(TestData.LOGIN_USER, TestData.PASSWORD_USER)
