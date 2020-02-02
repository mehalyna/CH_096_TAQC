"""
Api tests for getting chat with unread messages
"""
import pytest
import requests
import allure
from tests_api.config import URL_CHAT


@pytest.mark.usefixtures('fixture_chat_api')
class TestChat:
    """
    Testcase for getting chat through API that contain unread messages
    """

    @allure.link(
        "http://34.65.101.58:5002/user_chats",
        name='"Comuna" page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_chat_user_with_admin(self, header_user):
        """
        Test for getting user's chat, that contain unread messages
        """
        response = requests.get(
            URL_CHAT['unread_messages_user'],
            headers=header_user)
        res = response.json()
        mes_text = res[0]["text"]
        assert res[0]["text"] == "test message", f"Text don't equal to: {mes_text} "
        assert not res[0]["seen"]
        assert response.status_code == 200, "You have BAD REQUEST"
