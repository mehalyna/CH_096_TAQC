from Data.credentials import user,admin
from Locators.locators import ContactUsPageLocators




def test_contact_us(app):
    locator = ContactUsPageLocators
    app.signin.enter_actor(user['email'],user['password'])

    app.navigation.click_on_contact_us()
    app.base.element_be_clickable(locator.SUBMIT)
    app.contact.click_on_desc()
    app.navigation.click_on_contact_us()
    #mes = "Required"
    #self.assertTrue(self.exec.base.check_if_text_present(locator.REQUIRED, mes)), "not equal"








