"""Test create event"""
import allure
import pytest

from Data.credentials import user
from Data.test_data import CreateEventData
from Locators.locators import CreateEvent
from utilities.testLogging import PyLogging


event = CreateEventData
locator = CreateEvent

@allure.link("http://34.65.101.58:5002/home/events/?page=1")
@allure.feature('Create Event')
@allure.story("Create new event")
@pytest.mark.usefixtures("login")
def test_create_event(app):
    """
    Test create event
    """
    app.navigation.click_on_profile()
    app.prof_menu.click_on_add_event()
    app.creat_event.upload_image()
    app.creat_event.add_title(event.TITLE)
    text = event.DESCRIPTION['New Year']  # text add into description field for testing
    app.creat_event.add_desc(text)
    assert app.base.check_if_text_present(locator.DESC_TEXT, text)
    app.base.click_on_element(locator.CATEGORY)
    app.creat_event.add_category(locator.LST_CATEGORIES)
    app.base.click_action(0, 0)
    app.base.scroll_to_element(locator.COUNTRY_FIELD)
    app.creat_event.select_country(locator.COUNTRY_FIELD)
    app.base.click_on_element(locator.CITY)
    app.creat_event.select_city(locator.CITY)

    # app.creat_event.press_button_save( )
    #
    # app.base.check_if_element_exists( locator.SUCCESS_MSG )
    # app.base.get_element_text( locator.SUCCESS_MSG )









