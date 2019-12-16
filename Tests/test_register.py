from Tests.test_init import TestInit
from Locators.locators import RegisterLocators





class TestRegister(TestInit):

    def setUp(self):
        super().setUp()
        self.locator_reg = RegisterLocators


    def test_register_user(self):
        self.exec.signin.click_sign_in_up()
        self.exec.signin.click_on_register()
        self.assertTrue(self.exec.base.element_be_clickable(self.locator_reg.CLEAR)) , "element not clickable"
