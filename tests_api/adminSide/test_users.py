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
            self.User.edit_gender()
            self.assertEqual(
                self.User.get_gender(),
                self.gender,
                "Gender has not been changed to:{}".format(self.gender))

    def tearDown(self):
        with allure.step("Back user gender"):
            self.User.back_gender()
            self.assertEqual(
                self.User.get_gender(),
                self.base_gender,
                "Gender has not been changed to:{}".format(self.base_gender))


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
            self.User.edit_birthday()
            self.assertEqual(
                self.User.get_birthday(),
                self.birthday,
                "Birthday date has not been changed to:{}".format(
                    self.birthday))

    def tearDown(self):
        with allure.step("Back user birthday"):
            self.User.back_birthday()
            self.assertEqual(
                self.User.get_birthday(),
                self.base_birthday,
                "Birthday date has not been changed to:{}".format(
                    self.base_birthday))


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


class TestSetAttitude(unittest.TestCase):

    def setUp(self):
        self.id = "e02dfd94-a8a9-4b1a-6cfc-08d7a28d1878"
        self.name = "Jesus"
        self.gender = 2
        self.birthday = "2001-06-04"
        self.User = User(self.id, self.name, self.gender, self.birthday)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link(
        "http://34.65.101.58:5002/admin/users?page=1",
        name='Click me')
    def test_set_attitude(self):
        id = "038f157b-c102-4578-6cfb-08d7a28d1878"
        attitude=0
        with allure.step("Sett Attitude from user with ID {} to {}".format(self.id, id)):
            test = self.User.set_attitude(id, attitude)
            self.assertEqual(
                test.status_code,
                200,
                "Attitude {} was nor added".format(
                    attitude))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
