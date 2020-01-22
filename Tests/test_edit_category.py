import allure
from utilities.testLogging import PyLogging
from Data.test_data import CategoriesPage


@allure.link(
    "https://eventsexpress20200103054152.azurewebsites.net/",
    name='Click me')
@allure.feature('Login User')
@allure.story('Test editing category')
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_category(app, login_admin, screenshot_on_failure):
    """
    Test possibility to create , edit and delete category.
    """
    category_old = CategoriesPage.category_old
    category_new = CategoriesPage.category_new
    loger = PyLogging(__name__)
    loger.info("New test:")
    messages = ("Go to Categories page.",
                "Creating Category {}.".format(category_old),
                "Editing Category {} to {}".format(category_old, category_new))
    messages_error = (
        "Category {} was not created".format(category_old),
        "Category {} was not edited to {}".format(
            category_old,
            category_new),
        "Test Failed")
    with allure.step(messages[0]):
        try:
            loger.info(messages[0])
            app.navigation.click_on_categories()
        except Exception:
            loger.exception("")
            assert False, "Fail"
    with allure.step(messages[1]):
        try:
            loger.info(messages[1])
            app.categories.add_category(category_old)
            if app.categories.check_category_added(category_old):
                test1 = True
            else:
                test1 = False
                assert test1, messages_error[0]
        except Exception:
            loger.error(messages_error[0])
            loger.exception(messages_error[0])
            assert False, messages_error[0]
    with allure.step(messages[2]):
        try:
            loger.info(messages[2])
            app.categories.edit_category(category_old, category_new)
            if app.categories.check_category_added(category_new):
                test2 = True
                loger.info("Done!")
            else:
                test2 = False
                assert test2, messages_error[1]
        except Exception:
            loger.error(messages_error[1])
            loger.exception(messages_error[1])
            assert False, messages_error[1]
    # loger.sendreport()

    # teardown
    app.categories.delete_category(category_new)
    loger.info("Exit")
    print("Exit")
