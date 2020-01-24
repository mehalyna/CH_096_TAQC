import unittest
import requests
from tests_api.config import URL_CHAT
from tests_api.testHelper import Header


class TestChat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.header_user = Header().get_header_auth_user()
        cls.header_admin = Header().get_header_auth_admin()

    def test_get_chat_user(self):
        response = requests.get(URL_CHAT['all_chats'], headers=self.header_user)
        resp = response.status_code
        print(resp)
        self.assertEqual(200, resp, "You have BAD REQUEST")

    def test_get_chat_admin(self):
        response = requests.get(URL_CHAT['all_chats'], headers=self.header_admin)
        resp = response.status_code
        print(resp)
        self.assertEqual(200, resp, "You have BAD REQUEST")

    def test_get_chat_unauth(self):
        response = requests.get(URL_CHAT['all_chats'])
        resp = response.status_code
        print(resp)
        self.assertEqual(401, resp, "Actual, you get a chat, but you not authorized")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()