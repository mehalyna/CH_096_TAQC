import allure
import unittest
import requests
from config import URL


class Data:
    """
    Testdata class storage as a dictionary
    """
    ROLES = {
        'url_roles': f"{URL['URL_HOST']}/api/Roles",
    }


class TestAuth(unittest.TestCase):
    """
    API test. Check 'Admin' and 'User' roles
    This method have to assert all roles
    """
    @classmethod
    def setUpClass(cls):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_roles(self):
        """
        API test. Check 'Admin' and 'User' roles
        This method have to return and assert all roles
        :return: assertion result
        """

        response = requests.get(Data.ROLES['url_roles'])
        resp = response.json()
        self.assertEqual(200, response.status_code,
                         "BAD REQUEST")

        roles = []
        for role in resp:
            roles.append(role['name'])
        self.assertEqual(['Admin', 'User'], roles,
                         "Incorrect role or roles quantity")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
