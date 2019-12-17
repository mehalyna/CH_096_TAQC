from Tests.test_main import TestInit
from Pages.ContactUs import ContactUsPage
from Data.TestData import TestData
from Pages.LoginPage import LoginPage


class TestContactUs(TestInit):

    def setUp(self):
        super().setUp()
        self.contact_us = LoginPage(self.driver)
        self.contact_us.login_user(TestData.LOGIN_USER, TestData.PASSWORD_USER)
        self.contact_us.check_log_in_user()



    def test_contact_us(self):
        self.contact = ContactUsPage(self.driver)
        self.contact.click_on_contact_us_tab()
        self.contact.enter_description(TestData.DESCRIPTION)
        self.contact.click_on_submit()
        mes = self.contact.text_from_message()
        print(mes)
        self.assertEqual("Failed", mes)