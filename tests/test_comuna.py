import pytest
import allure
from config import INFO_MESSAGE_COMUNA as info


@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Users communication')
@allure.story('User have ability to send messages')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("login_admin")
def test_send_message(app):
    with allure.step("open communication page"):
        app.comuna.click_on_comuna()
        app.comuna.click_on_user_dialog()
        app.comuna.type_message(info['message_to_sent'])
        app.comuna.click_send()


@allure.link("http://34.65.101.58:5002/home/events?page=1", name='Click me')
@allure.feature('Users communication')
@allure.story('User have ability to receive messages')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("login")
def test_receive_message(app):
    app.comuna.click_on_comuna()
    assert app.comuna.get_text_of_notify() == info['verify_message']
