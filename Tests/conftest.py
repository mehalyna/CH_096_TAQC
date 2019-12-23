import pytest
from Driver.driver import Driver
from Data.credentials import user,admin
from Data.test_data import Config
from utilities.testFrame import InitPagesDriver




@pytest.fixture(scope='function')
def driver_init():
    driver = Driver(Config.BROWSER).set_browser()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Config.HOME_URL)
    return driver



@pytest.fixture(scope='function')
def app(driver_init):
    init_pages = InitPagesDriver(driver_init)
    yield init_pages
    driver_init.quit()


"""
@pytest.fixture(scope='function')
def get_to_user_profile(app):
    app.signin.enter_actor(admin['email'],admin['password'])
"""


