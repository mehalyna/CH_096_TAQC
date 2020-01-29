"""
Api tests for getting chat with unread messages
"""
import unittest
import requests
from tests_api.config import URL_CHAT
from tests_api.testHelper import Header
from dbconnection import Connection


class TestChat(unittest.TestCase):
    """
    Testcase for getting chat through API that contain unread messages
    """

    @classmethod
    def setUpClass(cls):
        cls.header_user = Header().get_header_auth_user()
        cls.header_admin = Header().get_header_auth_admin()
        cls.create_mes = Connection().send_message()

    def test_chat_user_with_admin(self):
        """
        Test for getting user's chat, that contain unread messages
        :return:
        """
        response = requests.get(
            URL_CHAT['unread_messages_user'],
            headers=self.header_user)
        res = response.json()
        mes_text = res[0]["text"]
        self.assertEqual(res[0]["text"], "test message", f"Text don't equal to: {mes_text} ")
        self.assertEqual(res[0]["seen"], False)
        self.assertEqual(200, response.status_code, "You have BAD REQUEST")

    @classmethod
    def tearDownClass(cls):
        cls.del_mes = Connection().delete_mes_with_text()


if __name__ == '__main__':
    unittest.main()
