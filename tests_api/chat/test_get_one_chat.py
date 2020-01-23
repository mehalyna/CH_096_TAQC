import unittest
import requests
import json
from tests_api.config import URL_CHAT, URL_AUTH,AUTH_PAYLOADS, HEADER
from tests_api.testHelper import Header


class TestChat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.header_user = Header().get_header_auth_user()
        cls.header_admin = Header().get_header_auth_admin()

    def test_chat_user_with_admin(self):
        response = requests.get(URL_CHAT['get_chat'], headers=self.header_user)
        resp = response.json()
        self.assertEqual(resp["id"], URL_CHAT['id'], "You can't get chat")
        self.assertEqual(200, response.status_code, "You have BAD REQUEST")

    def test_chat_admin_with_user(self):
        response = requests.get(URL_CHAT['get_chat'], headers=self.header_admin)
        resp = response.json()
        self.assertEqual(resp["id"], URL_CHAT['id'], "You can't get chat")
        self.assertEqual(200, response.status_code, "You have BAD REQUEST")

    def test_chat_unauth(self):
        response = requests.get(URL_CHAT['get_chat'])
        resp = response.status_code
        self.assertEqual(401, resp, "Actual, you get a chat, but you not authorized")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()