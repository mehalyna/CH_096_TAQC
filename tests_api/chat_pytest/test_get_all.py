"""
Api tests for getting all chats
"""
import requests
import allure
import pytest
from tests_api.config import URL_CHAT


@pytest.mark.usefixtures('fixture_chat_api')
class TestChat:
    """
    Testcase for getting all chats through API
    """

    @allure.link(
        "http://34.65.101.58:5002/user_chats",
        name='"Comuna" page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_chat_user(self, header_user):
        """
        Test for getting all user's chats
        """
        response = requests.get(
            URL_CHAT['all_chats'],
            headers=header_user)
        resp = response.status_code
        res = response.json()
        sender_name = res[0]['users'][0]['username']
        assert sender_name == "Admin", f"You can't get all chat as user {sender_name}"
        assert resp == 200, "You have BAD REQUEST"

    def test_get_chat_admin(self, header_admin):
        """
        Test for getting all admin's chats
        """
        response = requests.get(
            URL_CHAT['all_chats'],
            headers=header_admin)
        resp = response.status_code
        res = response.json()
        sender_name = res[0]['users'][1]['username']
        assert sender_name == "UserTest", f"You can't get all chat as user {sender_name}"
        assert resp == 200, "You have BAD REQUEST"

    def test_get_chat_unauth(self):
        """
        Negative test for getting all chats, when user not authorized
        """
        response = requests.get(URL_CHAT['all_chats'])
        resp = response.status_code
        assert resp == 401, "Actual, you get a chat, but you not authorized"
