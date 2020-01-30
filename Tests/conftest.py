import pytest
import allure
from utilities.testLogging import PyLogging
from allure_commons.types import AttachmentType
from driver.driver import Driver
from config import CREDENTIALS, URL

from pages.init_pages import InitPages
from dbconnection import Connection

@pytest.fixture(scope='function')
def driver_init(request):
    """
    Instantiate webdriver for selected browser and open homepage
    """
    driver = Driver(URL['Browser']).set_browser(URL['Test_mode'])
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get(URL['Home_URL'])
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope='function')
def app(driver_init):
    """
    Instantiate page objects for POM
    """
    page_init = InitPages(driver_init)
    return page_init


@pytest.fixture(scope='function')
def login(app):
    """
    Login as an user
    """
    with allure.step('Login as a user'):
        app.signin.enter_actor(CREDENTIALS['User_name'], CREDENTIALS['User_password'])
        loger=PyLogging(__name__)
        loger.info("Login as User")


@pytest.fixture(scope='function')
def login_admin(app):
    """
    Login as an admin
    """
    with allure.step('Login as an admin'):
        app.signin.enter_actor(CREDENTIALS['Admin_name'], CREDENTIALS['Admin_password'])
        loger = PyLogging(__name__)
        loger.info("Login as Admin")


@pytest.fixture(scope='function')
def create_event():
    """
    Create event
    """
    with allure.step('Create event'):
        db = Connection()
        db.create_event()
        loger = PyLogging(__name__)
        loger.info("Create Event")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook the "item" object on a test failure
    """
    # will execute even before the tryfirst one above!
    # do nothing here intentionally
    outcome = yield
    # will execute after all non-hookwrappers executed
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    # we only look at actual failing test calls, not setup/teardown
    # https://docs.pytest.org/en/latest/example/simple.html#post-process-test-reports-failures


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver_init):
    """
    Make screenshot on a test failure
    """
    # Intentionally blank section
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    with allure.step('Make screenshot'):
        if request.node.rep_setup.failed:
            print("setting up a test failed!", request.node.nodeid)
            allure.attach(driver_init.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=AttachmentType.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                print("executing test failed", request.node.nodeid)
                allure.attach(driver_init.get_screenshot_as_png(),
                              name=request.function.__name__,
                              attachment_type=AttachmentType.PNG)

@pytest.fixture(scope='function')
def delete_registered_user():
    """
    Delete user
    """
    yield
    with allure.step('Delete registered user'):
        db = Connection()
        db.delete_user_with_email("katya@gmail.com")
        loger = PyLogging(__name__)
        loger.info("Deleting user")
        db.close()

    
@pytest.fixture(scope='function')
def delete_event():
    """
    Delete event
    """
    yield
    with allure.step('Create event'):
        db = Connection()
        db.delete_event_with_name ("Test Event")
        loger = PyLogging(__name__)
        loger.info("Delete event")