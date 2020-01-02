from utilities.testLogging import TestLogging
from Locators.locators import ContactUsPageLocators as locator
from Data.test_data import ContactUsData as result
import allure


@allure.feature("Message 'Required'")
@allure.link("http://localhost:50621/contactUs", name='Click me')
@allure.story("Test appearance message 'Required'")
@allure.severity(allure.severity_level.CRITICAL)
def test_contact_us_clear(app, login, screenshot_on_failure):
    loger = TestLogging(__name__)
    loger.infos.append("New test:")
    messages = ("Go to 'Contact us' page.",
                "Check type of a list",
                "Enter description",
                "Click on 'Clear' button",
                "Test Passed")
    messages_error = ("Test Failed")

    with allure.step(messages[0]):
        app.navigation.click_on_contact_us()
        loger.infos.append(messages[0])
    app.base.element_be_clickable(locator.SUBMIT)
    with allure.step(messages[1]):
        app.contact.check_type()
        loger.infos.append(messages[1])
    with allure.step(messages[2]):
        app.contact.enter_description()
        loger.infos.append(messages[2])
    with allure.step(messages[3]):
        app.base.click_on_element(locator.CLEAR)
        loger.infos.append(messages[3])
    #assert(app.base.get_element_text(locator.DESCRIPTION) == result.EMPTY_RESULT)
    if (app.base.get_element_text(locator.DESCRIPTION) == result.EMPTY_RESULT):
        loger.infos.append(messages[4])
    else:
        loger.criticals.append(messages_error[0])
    loger.sendreport()







