import allure
import pytest
from Locators.locators import CreateEvent as Locator
from Locators.locators import HomePageLocators as LocHome
from config import CREATE_EVENT as Event
from dbconnection import Connection


# variable for checking if success message is available
MESSAGE = "Your event was created!"
# list for adding categories into category field
CAT_LIST = ['Summer', 'Golf', 'Swimming']
CAT_LIST1 = ['Mount', 'Gaming', 'Swimming']


@allure.link("http://34.65.101.58:5002/home/events/?page=1")
@allure.feature('Create Event')
@allure.story("Create new event")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login")
def test_create_event(app):
    """
    Test create event
    """
    app.navigation.click_on_profile()
    app.prof_menu.click_on_add_event()
    app.creat_event.upload_image()
    app.creat_event.add_title(Event['title'])
    # text add into description field for testing
    text = Event['description1']
    app.creat_event.add_desc(text)
    assert app.base.check_if_text_present(
        Locator.DESC_TEXT, text), "description doesn't match"
    app.base.click_on_element(Locator.CATEGORY)
    app.creat_event.add_category(CAT_LIST1, Locator.LST_CATEGORIES)
    app.base.click_action(0, 0)
    app.creat_event.add_date('02/06/2020')
    app.base.click_action(0, 0)
    app.base.scroll_to_element(Locator.COUNTRY_FIELD)
    app.base.click_on_element(Locator.COUNTRY_FIELD)
    app.base.select_visible_text(Locator.COUNTRY_FIELD, 'Taiwan')
    #app.creat_event.select_country(Locator.COUNTRY_FIELD)
    app.base.click_on_element(Locator.CITY)
    app.base.select_visible_text(Locator.CITY, 'Chi-lung')
    # app.creat_event.select_city(Locator.CITY)
    app.creat_event.press_button_save()
    app.base.check_if_element_exists(Locator.SUCCESS_MSG)
    msg = app.base.get_element_text(Locator.SUCCESS_MSG)
    assert str(msg) == MESSAGE, "success message was not wound"


@allure.link("http://34.65.101.58:5002/home/events/?page=1")
@allure.feature('Admin check if event created')
@allure.story("Create new event")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_admin")
def test_check_event_by_admin(app):
    """
     Test check if last created event is present (role admin)
     :param app: web driver
     :return:
     """
    app.home_page.check_pagination(LocHome.PAGINATION_BUTTONN)
    app.home_page.choose_last_event_title(
        Event['title'], LocHome.CART_TITLE_EVENT)
    assert app.base.check_if_text_present(
        LocHome.CART_TITLE_EVENT, 'Sensation WHITE'), "title of event doesn't match"
    app.home_page.choose_last_event_p(
        Event['description1'], LocHome.CART_P_EVENT)
    assert app.base.check_if_text_present(
        LocHome.CART_P_EVENT, Event['description1']), "title of event doesn't"


@allure.link("http://34.65.101.58:5002/home/events/?page=1")
@allure.feature('User check if event created')
@allure.story("check event")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login", "delete_event_ui")
def test_check_event_by_user(app):
    """
    Test check if last created event is present (role user)
    :param app: web driver
    :return:
    """
    app.home_page.check_pagination(LocHome.PAGINATION_BUTTONN)
    app.home_page.choose_last_event_title(
        Event['title'], LocHome.CART_TITLE_EVENT)
    assert app.base.check_if_text_present(
        LocHome.CART_TITLE_EVENT, "Sensation WHITE"), "title of event doesn't match"
    app.home_page.choose_last_event_p(
        Event['description1'], LocHome.CART_P_EVENT)
    assert app.base.check_if_text_present(
        LocHome.CART_P_EVENT, Event['description1']), "description of event doesn't"


