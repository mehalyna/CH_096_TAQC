from Data.credentials import user,admin
import pytest
import allure
from Data.test_data import CategoriesPage
@allure.link("http://localhost:57690/admin/categories/", name='Click me')
@allure.feature('Login User')
@allure.story('Test editing category')
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_category(app,login_admin,screenshot_on_failure):
    category_old = CategoriesPage.category_old
    category_new = CategoriesPage.category_new
    app.navigation.click_on_categories()
    app.categories.add_category(category_old)
    test1=app.categories.check_category_deleted(category_new)
    app.categories.edit_category(category_old, category_new)
    app.categories.check_category_added(category_new)
    #test2=app.categories.check_category_added('Hello2')
    test2 = app.categories.check_category_added(category_new)
    if test1 and test2:
        test3=True
    else:
        test3=False
    print (test3)
    assert test3, 'Testing assertion error... Good'

    #teardown
    app.categories.delete_category(category_new)
