"""
Api tests for getting only one chat
"""
import unittest
import requests
from tests_api.config import URL_CHAT
from tests_api.testHelper import Header
from dbconnection import Connection


class TestChat(unittest.TestCase):
    """
    Testcase for getting only one chat through API
    """

    @classmethod
    def setUpClass(cls):
        cls.header_user = Header().get_header_auth_user()
        cls.header_admin = Header().get_header_auth_admin()
        cls.create_mes = Connection().send_message()

    def test_chat_user_with_admin(self):
        """
        Test for getting user's chat with admin
        :return:
        """
        response = requests.get(URL_CHAT['get_chat'], headers=self.header_user)
        resp = response.json()
        print(resp)
        self.assertEqual(resp["id"], URL_CHAT['id'], "You can't get chat")
        self.assertEqual(200, response.status_code, "You have BAD REQUEST")

    def test_chat_admin_with_user(self):
        """
        Test for getting admin's chat with user
        :return:
        """
        response = requests.get(
            URL_CHAT['get_chat'],
            headers=self.header_admin)
        resp = response.json()
        self.assertEqual(resp["id"], URL_CHAT['id'], "You can't get chat")
        self.assertEqual(200, response.status_code, "You have BAD REQUEST")

    def test_chat_unauth(self):
        """
        Negative test for getting one chat, when user not authorized
        :return:
        """
        response = requests.get(URL_CHAT['get_chat'])
        resp = response.status_code
        self.assertEqual(
            401, resp, "Actual, you get a chat, but you not authorized")

    @classmethod
    def tearDownClass(cls):
        cls.del_mes = Connection().delete_mes_with_text()


if __name__ == '__main__':
    unittest.main()
