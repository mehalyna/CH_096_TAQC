import unittest
import allure
from tests_api.testHelper import User


class TestEditGender(unittest.TestCase):

    def setUp(self):
        self.id = "e02dfd94-a8a9-4b1a-6cfc-08d7a28d1878"
        self.name = "Jesus"
        self.gender = 2
        self.birthday = "2001-06-04"
        self.User = User(self.id, self.name, self.gender, self.birthday)
        self.base_gender = self.User.get_gender()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link(
        "http://34.65.101.58:5002/admin/users?page=1",
        name='Click me')
    def test_edit_g(self):
        with allure.step("Edit user gender"):
            self.User.edit_gender(self.gender)
            self.assertEqual(
                self.User.get_gender(),
                self.gender,
                "Gender has not been changed to:{}".format(self.gender))

    def tearDown(self):
        with allure.step("Back user gender"):
            self.User.edit_gender(self.base_gender)
            self.assertEqual(
                self.User.get_gender(),
                self.base_gender,
                "Gender has not been changed to:{}".format(self.base_gender))


if __name__ == '__main__':
    unittest.main()
