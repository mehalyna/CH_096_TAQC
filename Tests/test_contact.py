from Data.credentials import user,admin


def test_setup(app):
    app.signin.enter_actor(user['email'], user['password'])


def test_contact_us(app):
    app.navigation.click_on_contact_us()
    #app.base.element_be_clickable(app.locator.SUBMIT)
    app.contact.check_type()
    app.text = app.data.DESCRIPT
    app.contact.enter_description(app.text)
    app.contact.get_text_from_list()
    app.contact.click_on_submit()
    #self.error = "Failed"
    #self.assertTrue(self.exec.base.check_if_text_present(self.locator.MES, self.error)), "not equal"








