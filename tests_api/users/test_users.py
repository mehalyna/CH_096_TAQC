import allure
import unittest
import requests
import json
from config import URL
from tests_api.config import URL_AUTH, AUTH_PAYLOADS, HEADER
from tests_api.testHelper import Header


class Data:
    """
    Search and assert a user
    """
    WHAT = {
        'url_search_users': f"{URL['URL_HOST']}/api/Users/SearchUsers?page=1",
    }


class TestUsers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.header = Header().get_header_auth_admin()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_users(self):
        """
        API test. This method search for users
        Required userId string($uuid) and roleId string($uuid)
        :return: assertion result
        """

        # pre = Tools()
        # data = pre.get_user_data()

        response = requests.get(Data.WHAT['url_search_users'],
                                headers=self.header,
                                data=AUTH_PAYLOADS['payload_admin']
                                )
        resp = response #.json()

        self.assertEqual(200, response.status_code, "BAD REQUEST")

        users = []
        for user in resp['items']:
            users.append(user['username'])
        self.assertEqual(['Admin', 'UserTest'], users, "Wrong users")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
