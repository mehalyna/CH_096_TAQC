from utilities.testLogging import TestLogging
from Locators.locators import ContactUsPageLocators as locator
import allure


@allure.feature('Positive test')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("http://localhost:50621/contactUs", name='Click me')
@allure.story('Test sending message to admin')
def test_contact_us(app, login, screenshot_on_failure):
    loger = TestLogging(__name__)
    loger.infos.append("New test:")
    messages = ("Go to 'Contact us' page.",
                "Check type of a list",
                "Enter description",
                "Click on 'Submit' button",
                "Test Passed")
    messages_error = ("Test Failed, message don't send to admin ")

    with allure.step(messages[0]):
        app.navigation.click_on_contact_us()
        loger.infos.append(messages[0])
    app.base.element_be_clickable(locator.SUBMIT)
    with allure.step(messages[1]):
        app.contact.check_type()
        loger.infos.append(messages[1])
        app.contact.get_text_from_list()
    with allure.step(messages[2]):
        app.contact.enter_description()
        loger.infos.append(messages[2])
    with allure.step(messages[3]):
        app.base.click_on_element(locator.SUBMIT)
        loger.infos.append(messages[3])
    assert(app.contact.get_text_from_result() == True)
    #if (app.contact.get_text_from_result() == False):
    #   loger.criticals.append(messages_error[0])
    #else:
    #   loger.infos.append(messages[4])
    loger.sendreport()










