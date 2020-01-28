import unittest
import allure
from tests_api.testHelper import User


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
        attitude = 0
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
