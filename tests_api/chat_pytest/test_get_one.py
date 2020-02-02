"""
Api tests for getting only one chat
"""
import requests
import allure
import pytest
from tests_api.config import URL_CHAT


@pytest.mark.usefixtures('fixture_chat_api')
class TestChat:
    """
    Testcase for getting only one chat through API
    """

    @allure.link(
        "http://34.65.101.58:5002/user_chats",
        name='"Comuna" page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_chat_user_with_admin(self, header_user):
        """
        Test for getting user's chat with admin
        """
        response = requests.get(URL_CHAT['get_chat'], headers=header_user)
        resp = response.json()
        assert resp["id"] == URL_CHAT['id'], "You can't get chat"
        assert response.status_code == 200, "You have BAD REQUEST"

    def test_chat_admin_with_user(self, header_admin):
        """
        Test for getting admin's chat with user
        """
        response = requests.get(
            URL_CHAT['get_chat'],
            headers=header_admin)
        resp = response.json()
        assert resp["id"] == URL_CHAT['id'], "You can't get chat"
        assert response.status_code == 200, "You have BAD REQUEST"

    def test_chat_unauth(self):
        """
        Negative test for getting one chat, when user not authorized
        """
        response = requests.get(URL_CHAT['get_chat'])
        resp = response.status_code
        assert resp == 401, "Actual, you get a chat, but you not authorized"
