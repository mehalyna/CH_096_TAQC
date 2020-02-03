"""Test possibility to create , edit and delete category."""
import allure
import pytest
from utilities.testLogging import loger
from config import CATEGORIESPAGE


@allure.link(
    "https://eventsexpress20200103054152.azurewebsites.net/",
    name='Click me')
@allure.feature('Login User')
@allure.story('Test editing category')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_admin")
@pytest.mark.usefixtures("create_category")
@pytest.mark.usefixtures("delete_category")
def test_edit_category(app):
    """
    Test possibility to edit an category
    """
    category_old = CATEGORIESPAGE['category_old']
    category_new = CATEGORIESPAGE['category_new']
    msg="New test:{}".format(__name__)
    loger('Category', 'info', msg)
    app.navigation.click_on_categories()
    app.categories.edit_category(category_old, category_new)
    if app.categories.check_category_added(category_new):
        loger('Category', 'info', 'Done!')
    else:
        msg="Category {} was not edited to {}".format(category_old, category_new)
        loger('Category', 'error', msg)
        assert False, "Category {} was not edited to {}".format(
            category_old, category_new)
    loger('Category', 'info', 'Test End')
    print("Exit")
