import allure
import unittest
import requests
from config import URL
from tests_api.testHelper import Header


class Data:
    """
    Search and assert all users
    """
    # urls for certain activities
    WHAT = {
        'url_search_users': f"{URL['URL_HOST']}/api/Users/SearchUsers?page=1",
        'url_users': f"{URL['URL_HOST']}/api/Users/Get?page=1",
        'url_unblock': f"{URL['URL_HOST']}/api/Users/Unblock?page=1",
        'url_block': f"{URL['URL_HOST']}/api/Users/Block?page=1",
    }


class TestUsers(unittest.TestCase):
    """
     API tests for
     :params: [search users, users, unblock, block]
     :return: assertion results
    """
    @classmethod
    def setUpClass(cls):
        cls.header = Header().get_header_auth_admin()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_users(self):
        """
        API test. This method search all users in the project' db
        Equivalent to browse Search User from navigation menu
        :return: assertion result
        """
        response = requests.get(Data.WHAT['url_search_users'],
                                headers=self.header)
        resp = response.json()
        self.assertEqual(200, response.status_code, "BAD REQUEST")

        users = []
        users_count = len(resp['items'])

        for index in range(users_count):
            users.append(resp['items'][index]['username'])

        self.assertEqual(['Admin', 'UserTest'], users, "Wrong users")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_users(self):
        """
        API test. Search for users in the project' db
        Equivalent to browse Users from navigation menu
        :return: assertion result
        """

        response = requests.get(Data.WHAT['url_users'],
                                headers=self.header)
        resp = response.json()
        self.assertEqual(200, response.status_code, "BAD REQUEST")

        users = []
        users_count = len(resp['items'])

        for index in range(users_count):
            users.append(resp['items'][index]['username'])

        self.assertEqual(['Admin', 'UserTest'], users, "Wrong users")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
