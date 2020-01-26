import json
import unittest
import requests
from dbconnection import Connection
from tests_api.config import URL_AUTH, AUTH_PAYLOADS, HEADER


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_login_admin(self):
        response_decoded_json = requests.post(URL_AUTH['url_login'], data=json.dumps(AUTH_PAYLOADS['payload_admin']),
                                              headers=HEADER['header'])
        resp = response_decoded_json.json()
        print(resp)
        self.assertEqual("Admin", resp["role"], "You don't login with correct role")
        self.assertEqual(200, response_decoded_json.status_code, "You have BAD REQUEST")

    def test_login_user(self):
        response_decoded_json = requests.post(URL_AUTH.url_login, data=json.dumps(AUTH_PAYLOADS.payload_user),
                                              headers=HEADER.header)
        resp = response_decoded_json.json()
        print(resp["role"])
        self.assertEqual("User", resp["role"], "You don't login with correct role")
        self.assertEqual(200, response_decoded_json.status_code, "You have BAD REQUEST")

    def test_unauthorized_user(self):
        response_decoded_json = requests.post(URL_AUTH.url_login, data=json.dumps(AUTH_PAYLOADS.payload_unauth),
                                              headers=HEADER.header)
        mes = response_decoded_json.json()
        self.assertEqual(400, response_decoded_json.status_code, "You have BAD REQUEST")

    def test_register_already_exist(self):
        response_decoded_json = requests.post(URL_AUTH.url_register, data=json.dumps(AUTH_PAYLOADS.payload_user),
                                              headers=HEADER.header)
        mes = response_decoded_json.json()
        self.assertEqual("Email already exists in database", mes, "There is no such email in the database")
        self.assertEqual(400, response_decoded_json.status_code, "You have BAD REQUEST")

    def test_register_new_user(self):
        response_decoded_json = requests.post(URL_AUTH.url_register, data=json.dumps(AUTH_PAYLOADS.payload_unauth),
                                              headers=HEADER.header)
        self.assertEqual(200, response_decoded_json.status_code)

    @classmethod
    def tearDownClass(cls):
        cls.conn = Connection()
        cls.conn.delete_user_with_email("katya@gmail.com")
        cls.conn.close()


if __name__ == '__main__':
    unittest.main()
