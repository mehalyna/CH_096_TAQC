"""
API tests for users item from navigation menu
"""
import unittest
import requests
import allure
from tests_api.config import URL_USERS
from tests_api.testHelper import Header
from tests_api.testHelper import EditUserByAdmin  # pylint: disable=import-error


# pylint: disable=too-few-public-methods
class Data:
    """
    urls for certain activities for
    api tests for search and assert all users
    """
    WHAT = URL_USERS
    USERNAME = 'Vasya'


class TestUsers(unittest.TestCase):
    """
     API tests for
     :params: [search users, users, unblock, block]
     :return: assertion results
    """
    @classmethod
    def setUpClass(cls):
        cls.header = Header().get_header_auth_admin()
        cls.user = EditUserByAdmin(Data.USERNAME)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_users(self):
        """
        API test. This method search all users in the project' db
        Equivalent to browse Search User from navigation menu
        :return: assertion result
        """
        response = requests.get(Data.WHAT['url_search_users'],
                                headers=self.header)
        self.assertEqual(200, response.status_code, "BAD REQUEST")

        # users = []
        # resp = response.json()
        # users_count = len(resp['items'])
        #
        # for index in range(users_count):
        #     users.append(resp['items'][index]['username'])
        users = self.user.collect_users(response)
        self.assertEqual(['Admin', 'UserTest', 'Jesus'], users, "Wrong users")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_users(self):
        """
        API test. Collect all users within the project' db
        Equivalent to browse Users from navigation menu
        :return: assertion result
        """

        response = requests.get(Data.WHAT['url_users'],
                                headers=self.header)

        self.assertEqual(200, response.status_code, "BAD REQUEST")

        actual_users = []
        resp = response.json()
        users_count = len(resp['items'])

        for index in range(users_count):
            actual_users.append(resp['items'][index]['username'])

        expected_users = ['Admin', 'UserTest', 'koq86', 'koc86', 'Jesus', 'boris.v.skip', 'user2']
        self.assertEqual(expected_users, actual_users, "Wrong users")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_block_user(self):
        """
        API test. Block a user
        Equivalent to browse Users from navigation menu
        :return: assertion result
        """

        response = requests.post(Data.WHAT['url_block_user'],
                                 data='user_id',
                                 headers=self.header)

        self.assertEqual(200, response.status_code, "BAD REQUEST")

        actual_users = []
        resp = response.json()
        users_count = len(resp['items'])

        for index in range(users_count):
            actual_users.append(resp['items'][index]['username'])

        expected_users = ['Admin', 'UserTest', 'koq86', 'koc86', 'Vasya']
        self.assertEqual(expected_users, actual_users, "Wrong users")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
