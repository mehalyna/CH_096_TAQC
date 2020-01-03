from Data.credentials import user,admin
from Data.test_data import CreateEventData
from Locators.locators import CreateEvent



event = CreateEventData
locator = CreateEvent


def test_create_event(app):
    """
    Test check if user could create new event. And after filled all fields and press
    button 'save' success message will appear
    :param app:
    :return: True if success msg is available
    """
    app.signin.enter_actor( user['email'], user['password'] )
    app.navigation.click_on_profile( )
    app.prof_menu.click_on_add_event( )
    app.creat_event.upload_image( )
    app.creat_event.add_title( event.TITLE )
    text = event.DESCRIPTION['New Year']  # text add into description field for testing
    app.creat_event.add_desc( text )
    #app.base.check_if_text_present( locator.DESC_TEXT, text ), 'Field for add description is not available'
    # self.exec.base.get_element_text(self.locator.DESC_TEXT)
    app.base.click_on_element( locator.CATEGORY )
    app.creat_event.add_category( locator.LST_CATEGORIES )
    app.base.click_action(0, 0)
    app.base.click_on_element( locator.COUNTRY_FIELD )
    app.creat_event.select_country( locator.COUNTRY_FIELD )
    app.base.click_on_element( locator.CITY )
    app.creat_event.select_city(locator.CITY)
    app.creat_event.press_button_save()
    assert app.base.check_if_element_exists( locator.SUCCESS_MSG ), 'Message for reported about success created event is not available'
    # app.base.get_element_text( locator.SUCCESS_MSG ), 'Text about success created event is not available was not get'









