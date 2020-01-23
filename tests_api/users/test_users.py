import allure
import pytest
import unittest
import requests
from config import URL


class Data:
    """
    Search and assert a user
    """
    WHAT = {
        'url_users': f"{URL['URL_HOST']}/api/Users/SearchUsers",
    }


class TestAuth(unittest.TestCase):

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
        roles = []
        response_decoded_json = requests.get(Data.WHAT['url_roles'])
        resp = response_decoded_json.json()
        self.assertEqual(200, response_decoded_json.status_code, "BAD REQUEST")

        for role in resp:
            roles.append(role['name'])
        self.assertEqual(['Admin', 'User'], roles, "Incorrect role or roles quantity")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
