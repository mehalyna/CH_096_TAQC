from Tests.test_main import TestLoginToSite
from Pages.ContactUs import ContactUsPage
from Data.TestData import TestData


class TestContactUs(TestLoginToSite):

    def setUp(self):
        super().setUp()



    def test_contact_us(self):
        self.contact_us_page = ContactUsPage(self.driver)
        self.contact_us_page.click_on_contact_us_tab()
        self.contact_us_page.enter_description(TestData.DESCRIPTION)
        self.contact_us_page.click_on_submit()
        mes = self.contact_us_page.text_from_message()
        print(mes)
        self.assertEqual("Failed", mes)