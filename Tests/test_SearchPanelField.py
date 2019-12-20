from Data.credentials import user,admin

def test_setup(app):
    app.signin.enter_actor(admin['email'],admin['password'])


def test_search_event(app):
    app.search.type_in_search_field('Python MeetUp')
    app.search.click_button_search()
