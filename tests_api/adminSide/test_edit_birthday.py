import unittest
import allure
from tests_api.testHelper import User


class TestEditBirthday(unittest.TestCase):

    def setUp(self):
        self.id = "e02dfd94-a8a9-4b1a-6cfc-08d7a28d1878"
        self.name = "Jesus"
        self.gender = 2
        self.birthday = "2001-06-04"
        self.User = User(self.id, self.name, self.gender, self.birthday)
        self.base_birthday = self.User.get_birthday()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link(
        "http://34.65.101.58:5002/admin/users?page=1",
        name='Click me')
    def test_edit_b(self):
        with allure.step("Edit user birthday"):
            self.User.edit_birthday(self.birthday)
            self.assertEqual(
                self.User.get_birthday(),
                self.birthday,
                "Birthday date has not been changed to:{}".format(
                    self.birthday))

    def tearDown(self):
        with allure.step("Back user birthday"):
            self.User.edit_birthday(self.base_birthday)
            self.assertEqual(
                self.User.get_birthday(),
                self.base_birthday,
                "Birthday date has not been changed to:{}".format(
                    self.base_birthday))


if __name__ == '__main__':
    unittest.main()
