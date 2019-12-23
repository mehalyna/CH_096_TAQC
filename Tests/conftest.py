import pytest
import allure
from allure_commons.types import AttachmentType
import time

from Base.base import BaseSetup

from Driver.driver import Driver
from Data.test_data import Config
from utilities.testFrame import InitPages
from Data.test_data import CreateEventData


@pytest.fixture(scope='function')
def event():
    this_driver = Driver(Config.BROWSER).set_browser()
    this_driver.delete_all_cookies()
    # this.river.maximize_window()
    this_driver.implicitly_wait(10)
    this_driver.get(Config.HOME_URL)
    # wrapping Selenium webdriver
    wrap_selenium = BaseSetup(this_driver)
    # do instantiate all classes
    wrapped_driver = InitPages(wrap_selenium)
    # do login
    # wrapped_driver.signin.enter_actor(CreateEventData.LOGIN_USER,
    #                              CreateEventData.PASSWORD_USER)
    yield wrapped_driver
    time.sleep(3)  # ToDo
    this_driver.close()
    this_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # will execute even before the tryfirst one above! ?without (tryfirst=True, hookwrapper=True)
    # do nothing here intentionally
    outcome = yield
    # will execute after all non-hookwrappers executed
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    # we only look at actual failing test calls, not setup/teardown
    # https://docs.pytest.org/en/latest/example/simple.html#post-process-test-reports-failures

@pytest.fixture
def screenshot_on_failure(event, request):
    #
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed: # if rep.when == "call" and rep.failed:
        print("setting up a test failed!", request.node.nodeid)
        allure.attach(event.get_screenshot_as_png(),
                      # name = request.function.__name__,
                      name='/home/stable/Documents/Automation_SS/Python/CH_096_TAQC/Reports_Allure/Screenshot',
                      attachment_type = allure.attachment_type.PNG)
        # from allure_commons.types import AttachmentType
        #
        # allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        # allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)

    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            print("executing test failed", request.node.nodeid)
            allure.attach(event.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)



# https://stackoverflow.com/questions/49576504/pytest-allure-screenshot-of-failure-in-allure-report

'''@allure.feature('Attachments')
def test_multiple_attachments():
    allure.attach.file('./data/totally_open_source_kitten.png', attachment_type=allure.attachment_type.PNG)
    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)'''

'''
@pytest.fixture(scope='function')
def get_driver():
    print('===============setUp===================')
    driver = Driver(Config.BROWSER).set_browser()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Config.HOME_URL)
    wrapped_driver = BaseSetup(driver)
    return wrapped_driver

    # def teardown_module(self):
    #     print('===============teardown===================')
    #     time.sleep(3)  # ToDo
    #     driver.close()
    #     driver.quit()

@pytest.fixture(scope='function')
def event(get_driver):
    event_init = InitPagesDriver(get_driver)
    return event_init
'''
