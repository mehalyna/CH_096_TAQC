import pytest
import allure


@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Users communication')
@allure.story('User have ability to send messages')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("login_admin")
def test_send_message(app):
    with allure.step("open communication page"):
        app.comuna.click_on_comuna()
        app.comuna.click_on_user_dialog()
        app.comuna.type_message("hey")
        app.comuna.click_send()


@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Users communication')
@allure.story('User have ability to receive messages')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("login")
def test_receive_message(app):
    app.comuna.click_on_comuna()
    assert app.comuna.get_text_of_notify() == "You have 1 unread messages"
