from Data.credentials import user,admin

# def test_setup(app):
#     app.signin.enter_actor(admin['email'],admin['password'])


def test_search_event(app):
    app.signin.enter_actor( admin['email'], admin['password'] )
    app.search.open_filter()
    app.search.enter_date_from('12/19/19')
    app.search.enter_date_to('12/20/19')
    #self.exec.search.click_to_categories()
    app.search.click_button_search()
    #self.assertEqual(self.exec.search.check_name_event(), "test")
