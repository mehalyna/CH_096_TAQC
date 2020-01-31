"""
Api tests for getting all chats
"""
import unittest
import requests
import allure
from tests_api.config import URL_CHAT
from tests_api.testHelper import Header
from dbconnection import Connection


class TestChat(unittest.TestCase):
    """
    Testcase for getting all chats through API
    """

    @classmethod
    def setUpClass(cls):
        cls.header_user = Header().get_header_auth_user()
        cls.header_admin = Header().get_header_auth_admin()
        cls.create_mes = Connection().send_message()

    @allure.link(
        "http://34.65.101.58:5002/contactUs",
        name='"Contact us" page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_chat_user(self):
        """
        Test for getting all user's chats
        """
        response = requests.get(
            URL_CHAT['all_chats'],
            headers=self.header_user)
        resp = response.status_code
        res = response.json()
        sender_name = res[0]['users'][0]['username']
        self.assertEqual(
            "Admin",
            sender_name,
            f"You can't get all chat as user {sender_name}")
        self.assertEqual(200, resp, "You have BAD REQUEST")

    def test_get_chat_admin(self):
        """
        Test for getting all admin's chats
        """
        response = requests.get(
            URL_CHAT['all_chats'],
            headers=self.header_admin)
        resp = response.status_code
        res = response.json()
        sender_name = res[0]['users'][1]['username']
        self.assertEqual(
            "UserTest",
            sender_name,
            f"You can't get all chat as user {sender_name}")
        self.assertEqual(200, resp, "You have BAD REQUEST")

    def test_get_chat_unauth(self):
        """
        Negative test for getting all chats, when user not authorized
        """
        response = requests.get(URL_CHAT['all_chats'])
        resp = response.status_code
        self.assertEqual(
            401, resp, "Actual, you get a chat, but you not authorized")

    @classmethod
    def tearDownClass(cls):
        cls.del_mes = Connection().delete_mes_with_text()


if __name__ == '__main__':
    unittest.main()
