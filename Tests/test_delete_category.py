"""test create event"""
import allure
from Data.test_data import CategoriesPage


@allure.link("http://34.65.101.58:5002/admin/categories/", name='Click me')
@allure.feature('Login Admin')
@allure.story('Test deleting category')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_category(app, login_admin):
    """delete category"""
    category_old = CategoriesPage.category_old
    with allure.step("Go to Categories page."):
        app.navigation.click_on_categories()
    with allure.step("Creating Category."):
        app.categories.add_category(category_old)
        assert (app.categories.check_category_added(category_old)), "Category wasn't create"
    with allure.step("Deleting Category"):
        app.categories.delete_category(category_old)
        assert (app.categories.check_category_deleted(category_old)), "Category wasn't create"
