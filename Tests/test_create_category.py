from Tests.test_init import TestInit
from Data.credentials import user,admin






class TestCreateCategory(TestInit):


    def setUp(self):
        super().setUp()
        self.exec.signin.enter_actor(admin['email'], admin['password'])



    def test_create_category(self):
        self.category='hello'
        self.exec.navigation.click_on_categories()
        self.exec.categories.add_category(self.category)
        test=self.exec.categories.check_category_added(self.category)
        self.assertTrue(test)

    def tearDown(self):
        self.exec.categories.delete_category(self.category)
        super().tearDown()
