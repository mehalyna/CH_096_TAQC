import allure
import unittest
import requests
import json
from config import URL
from tests_api.config import URL_AUTH, AUTH_PAYLOADS, HEADER


class Data:
    """
    Search and assert a user
    """
    WHAT = {
        'url_chng_role': f"{URL['URL_HOST']}/api/Users/ChangeRole",
    }


class TestUsers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_chg_roles(self):
        """
        API test. This method have to change role of user
        Required userId string($uuid) and roleId string($uuid)
        :return: assertion result
        """
        pre = Tools()
        data = pre.get_user_data()

        roles = []
        response = requests.post(Data.WHAT['url_chng_role'],
                                 headers=HEADER['header'],
                                 data=json.dumps(AUTH_PAYLOADS.payload_user)
                                 )
        resp = response.json()

        self.assertEqual(200, response.status_code, "BAD REQUEST")

        for role in resp:
            roles.append(role['name'])
        self.assertEqual(['Admin', 'User'], roles, "Incorrect role or roles quantity")

    @classmethod
    def tearDownClass(cls):
        pass


class Tools:

    @staticmethod
    def get_user_data():
        response = requests.post(URL_AUTH['url_login'],
                                 headers=HEADER['header'],
                                 data=json.dumps(AUTH_PAYLOADS.payload_user))

        resp = response.json()
        print(resp["id"], resp["role"], '\n', resp["token"], response.status_code)
        return {'id': resp["id"], 'role': resp["role"], 'token': response.status_code}


if __name__ == '__main__':
    unittest.main()