from Tests.test_init import TestInit
from Data.credentials import user,admin






class TestDeleteCategory(TestInit):


    def setUp(self):
        super().setUp()
        self.category='hello'
        self.exec.signin.enter_actor(admin['email'], admin['password'])
        self.exec.navigation.click_on_categories()
        self.exec.categories.add_category(self.category)



    def test_delete_category(self):
        self.exec.categories.check_category_added(self.category)
        self.exec.categories.delete_category(self.category)
        test=self.exec.categories.check_category_deleted(self.category)
        self.assertTrue(test)
