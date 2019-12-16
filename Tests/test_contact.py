from Tests.test_init import TestInit
from Data.credentials import user,admin






class TestContactUs(TestInit):

    def setUp(self):
        super().setUp()




    def test_contact_us(self):
        self.exec.signin.enter_actor(user['email'],user['password'])
        self.exec.navigation.click_on_contact_us()
        self.exec.contact.enter_description()
        self.exec.contact.click_on_submit()
        self.assertEqual("Failed", self.exec.contact.get_element_text())






