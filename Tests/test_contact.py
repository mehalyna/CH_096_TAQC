from Data.credentials import user,admin
from Locators.locators import ContactUsPageLocators
import allure


@allure.feature('Run test')
def test_contact_us(app):
    locator = ContactUsPageLocators
    app.signin.enter_actor(user['email'], user['password'])

    app.navigation.click_on_contact_us()
    app.base.element_be_clickable(locator.SUBMIT)
    app.contact.check_type()
    text = app.data.DESCRIPTION
    app.contact.enter_description(text)
    app.contact.get_text_from_list()
    app.contact.click_on_submit()
    error = "Failed"
    assert(app.base.get_element_text(locator.MES) == error)








