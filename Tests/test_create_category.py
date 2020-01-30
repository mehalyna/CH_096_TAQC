"""test create event"""
import allure
import pytest

from data.test_data import CategoriesPage


@allure.link("http://34.65.101.58:5002/admin/categories/", name='Click me')
@allure.feature('Login Admin')
@allure.story('Test creating category')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_admin")
def test_create_category(app):
    """test create category"""
    category_old = CategoriesPage.category_old
    with allure.step("Go to Categories page."):
        app.navigation.click_on_categories()
    with allure.step("Creating Category."):
        app.categories.add_category(category_old)
        assert (app.categories.check_category_added(category_old)), "Category wasn't create"
