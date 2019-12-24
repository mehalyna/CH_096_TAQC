from Data.credentials import user,admin
import pytest
import allure
from Data.test_data import CategoriesPage
@allure.link("http://localhost:57690/admin/categories/", name='Click me')
@allure.feature('Login User')
@allure.story('Test creating category')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_category(app,login_admin,screenshot_on_failure):
    category_old = CategoriesPage.category_old
    app.navigation.click_on_categories()
    app.categories.add_category(category_old)
    test1=app.categories.check_category_added(category_old)
    app.categories.delete_category(category_old)
    test2=app.categories.check_category_deleted(category_old)
    if test1 and test2:
        test3=True
    else:
        test3=False
    assert test3

    #teatdown
