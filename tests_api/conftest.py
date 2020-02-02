import pytest

from dbconnection import Connection
from tests_api.testHelper import Header


@pytest.fixture()
def header_admin():
    header = Header().get_header_auth_admin()
    return header


@pytest.fixture()
def get_conn():
    conn = Connection()
    return conn


@pytest.fixture(scope='class')
def delete_user_and_close_conn():
    yield
    conn = Connection()
    conn.delete_user_with_email("katya@gmail.com")
    conn.close()


@pytest.fixture(scope='class')
def fixture_category_api():
    conn = Connection()
    conn.create_category_with_name("category to be deleted")
    yield
    conn = Connection()
    conn.delete_category_with_name("new")
    conn.delete_category_with_name("category to be deleted")
    conn.edit_category_with_name("MountNew", "Mount")
    conn.close()

# @pytest.fixture(scope='class')
# def teardown_for_category():
#     yield
#     conn = Connection()
#     conn.delete_category_with_name("new")
#     conn.delete_category_with_name("category to be deleted")
#     conn.edit_category_with_name("MountNew", "Mount")
#     conn.close()
