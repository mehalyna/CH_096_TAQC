from Tests.test_init import TestInit
from Data.credentials import user,admin






class TestCreateEvent(TestInit):


    def setUp(self):
        super().setUp()




    def test_create_category(self):
        self.exec.signin.enter_actor(admin['email'],admin['password'])
        category='hello'
        self.exec.navigation.click_on_categories()
        self.exec.categories.add_category(category)
        t1=self.exec.categories.check_category_added(category)
        self.exec.categories.delete_category(category)
        t2=self.exec.categories.check_category_deleted(category)
        if t1 and t2:
            t3=True
        else:
            t3=False
        self.assertTrue(t3)
