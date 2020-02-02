import pytest

from dbconnection import Connection
from tests_api.testHelper import Header


@pytest.fixture(scope='class')
def header_admin_and_connect_db():
    header = Header().get_header_auth_admin()
    return header


@pytest.fixture(scope='class')
def delete_user_and_close_conn():
    yield
    conn = Connection()
    conn.delete_user_with_email("katya@gmail.com")
    conn.close()
