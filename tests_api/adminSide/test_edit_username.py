import unittest
import allure
from tests_api.testHelper import User


class TestEditUsername(unittest.TestCase):

    def setUp(self):
        self.id = "e02dfd94-a8a9-4b1a-6cfc-08d7a28d1878"
        self.name = "Jesus"
        self.gender = 2
        self.birthday = "2001-06-04"
        self.User = User(self.id, self.name, self.gender, self.birthday)
        self.base_username = self.User.get_username()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link(
        "http://34.65.101.58:5002/admin/users?page=1",
        name='Click me')
    def test_edit_u(self):
        with allure.step("Edit username"):
            self.User.edit_username()
            self.assertEqual(
                self.User.get_username(),
                self.name,
                "Username has not been changed to:{}".format(self.name))

    def tearDown(self):
        with allure.step("Back username"):
            self.User.back_username()
            self.assertEqual(
                self.User.get_username(),
                self.base_username,
                "Username has not been changed to:{}".format(
                    self.base_username))


if __name__ == '__main__':
    unittest.main()
