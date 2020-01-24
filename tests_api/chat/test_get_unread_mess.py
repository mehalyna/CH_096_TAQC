import unittest
import requests
import json
from tests_api.config import URL_CHAT, URL_AUTH, AUTH_PAYLOADS, HEADER
from tests_api.testHelper import Header


class TestChat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.header_user = Header().get_header_auth_user()
        cls.header_admin = Header().get_header_auth_admin()

    def test_chat_user_with_admin(self):
        response_decoded_json = requests.post(URL_AUTH['url_login'], data=json.dumps(AUTH_PAYLOADS['payload_admin']),
                                              headers=HEADER['header'])
        resp = response_decoded_json.json()
        print(resp['id'])
        response = requests.get(URL_CHAT['unread_messages_user'], headers=self.header_user)
        res = response.json()
        print(res[0]["senderId"])
        self.assertEqual(res[0]["text"], "how are u?")
        self.assertEqual(res[0]["seen"], False)
        self.assertEqual(resp["id"], res[0]["senderId"], "You can't get chat")
        self.assertEqual(200, response.status_code, "You have BAD REQUEST")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()