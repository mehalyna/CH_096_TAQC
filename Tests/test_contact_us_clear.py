from Tests.conftest import TestInit
from Data.credentials import user,admin
from Locators.locators import ContactUsPageLocators
from Data.test_data import ContactUsData






class TestContactUs(TestInit):

    def setUp(self):
        super().setUp()
        self.locator = ContactUsPageLocators
        self.data = ContactUsData




    def test_contact_us(self):
        self.exec.signin.enter_actor(user['email'],user['password'])
        self.exec.navigation.click_on_contact_us()
        self.exec.base.element_be_clickable(self.locator.SUBMIT)
        self.exec.contact.check_type()
        self.exec.contact.get_text_from_list()
        self.text = self.data.DISCRIPTION
        self.exec.contact.enter_description(self.text)
        self.exec.contact.click_on_clear()
        self.assertTrue(self.exec.base.check_if_text_present(self.locator.DESCRIPTION, "")), "not equal"








