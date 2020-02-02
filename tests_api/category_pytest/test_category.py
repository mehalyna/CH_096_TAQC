import json
import allure
import pytest
import requests
from tests_api.config import URL_CATEGORY, CATEGORY_PAYLOADS


@pytest.mark.usefixtures('fixture_category_api')
class TestCategoryAdminSide:

    @allure.feature("Get all category api")
    @allure.story('Admin have an ability to see all categories in EventExpress site')
    @allure.severity(allure.severity_level.NORMAL)
    def test_category_get_all(self, header_admin):
        response_decoded_json = requests.get(
            URL_CATEGORY['url_category_all'], headers=header_admin)
        r = [i['name'] for i in response_decoded_json.json()]
        assert 'Sea' in r
        assert 200 == response_decoded_json.status_code, 'Get all category endpoint goes wrong'

    @allure.feature("Edit category api")
    @allure.story('Admin have an ability to edit categories in EventExpress site')
    @allure.severity(allure.severity_level.NORMAL)
    def test_category_edit_mount(self, header_admin, get_conn):
        response_decoded_json = requests.post(
            URL_CATEGORY['url_category_edit'], data=json.dumps(
                CATEGORY_PAYLOADS['category_to_edit']), headers=header_admin)
        id = get_conn.get_name_of_category_using_id(CATEGORY_PAYLOADS['category_to_edit']['Id'])
        assert id == CATEGORY_PAYLOADS['category_to_edit']['Name']
        assert 200 == response_decoded_json.status_code

    @allure.feature("Create category api")
    @allure.story('Admin have an ability to create new category in EventExpress site')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_category(self, header_admin, get_conn):
        response_decoded_json = requests.post(
            URL_CATEGORY['url_category_edit'], data=json.dumps(
                CATEGORY_PAYLOADS['category_to_create']), headers=header_admin)
        id = get_conn.get_id_using_name(CATEGORY_PAYLOADS['category_to_create']['Name'])
        assert id is not None
        assert 200 == response_decoded_json.status_code

    @allure.feature("Delete category api")
    @allure.story('Admin have an ability to delete categoryc in EventExpress site')
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_category(self, header_admin, get_conn):
        id = get_conn.get_id_using_name("category to be deleted")
        response_decoded_json = requests.post(
            URL_CATEGORY['url_category_delete'] +
            id, headers=header_admin)
        assert str(0) == get_conn.get_count_of_category_on_name("category to be deleted")
        assert 200 == response_decoded_json.status_code
