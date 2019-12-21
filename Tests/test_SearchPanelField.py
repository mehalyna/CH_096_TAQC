from Data.credentials import user,admin

def test_search_event(app):
    app.signin.enter_actor(admin['email'],admin['password'])
    app.search.type_in_search_field('Python MeetUp')
    app.search.click_button_search()
