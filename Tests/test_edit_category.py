from Data.credentials import user,admin
from Data.test_data import CategoriesPage
import allure

@allure.feature("Run test")
def test_edit_category(app):
    category_old = CategoriesPage.category_old
    category_new = CategoriesPage.category_new
    app.signin.enter_actor(admin['email'], admin['password'])
    app.navigation.click_on_categories()
    app.categories.add_category(category_old)

    test1=app.categories.check_category_deleted(category_new)
    app.categories.edit_category(category_old, category_new)
    app.categories.check_category_added(category_new)
    test2=app.categories.check_category_added(category_new)
    if test1 and test2:
        test3=True
    else:
        test3=False
    print (test3)
    #self.assertTrue(test3)

    #teardown
    app.categories.delete_category(category_new)
