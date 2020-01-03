from Data.credentials import user,admin
from Locators.locators import SearchUsers, ComunaPageLocators


locator = SearchUsers
loc_com = ComunaPageLocators
name = 'Admin'
msg = "Hello Admin"


def test_communa(app):
    app.navigation.click_on_search_user()
    app.communa.chose_respond(name)
    app.base.click_on_element(locator.LOGO_PR)
    app.base.click_on_element( locator.LOGO_WR)
    app.base.click_on_element( loc_com.INPUT_FIELD )
    app.base.send_keys_to_element(loc_com.SEND_MESSAGE_FIELD,msg)
    app.communa.check_received_msg()

    # app.base.click_on_element(loc_com.SEND_BUTTON)



