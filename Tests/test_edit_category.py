from Tests.testinit import TestInit
from Data.credentials import user,admin






class TestEditCategory(TestInit):


    def setUp(self):
        super().setUp()
        self.category_old='hello'
        self.category_new='hello1'
        self.exec.signin.enter_actor(admin['email'], admin['password'])
        self.exec.navigation.click_on_categories()
        self.exec.categories.add_category(self.category_old)



    def test_edit_category(self):
        test1=self.exec.categories.check_category_deleted(self.category_new)
        self.exec.categories.edit_category(self.category_old, self.category_new)
        self.exec.categories.check_category_added(self.category_new)
        test2=self.exec.categories.check_category_added(self.category_new)
        if test1 and test2:
            test3=True
        else:
            test3=False
        self.assertTrue(test3)

    def tearDown(self):
        self.exec.categories.delete_category(self.category_new)
        super().tearDown()
