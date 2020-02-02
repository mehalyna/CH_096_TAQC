import json

import allure
import requests
import pytest

from tests_api.config import URL_AUTH, AUTH_PAYLOADS, HEADER


@pytest.mark.usefixtures('header_admin_and_connect_db')
@pytest.mark.usefixtures('delete_user_and_close_conn')
class TestSomething:
    @allure.feature("Login admin api")
    @allure.story('Admin have an ability to login in EventExpress site')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_admin(self):
        response_decoded_json = requests.post(URL_AUTH['url_login'], data=json.dumps(AUTH_PAYLOADS['payload_admin']),
                                              headers=HEADER['header'])
        resp = response_decoded_json.json()
        assert "Admin" == resp["role"], "You don't login with correct role"
        assert 200 == response_decoded_json.status_code, "You have BAD REQUEST"

    @allure.feature("Login user api")
    @allure.story('User have an ability to login in EventExpress site')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user(self):
        response_decoded_json = requests.post(URL_AUTH['url_login'], data=json.dumps(AUTH_PAYLOADS['payload_user']),
                                              headers=HEADER['header'])
        resp = response_decoded_json.json()
        assert "User" == resp["role"], "You don't login with correct role"
        assert 200 == response_decoded_json.status_code, "You have BAD REQUEST"

    @allure.feature("Login as unauthorized api")
    @allure.story('Unauthorized user does not have an ability to login in EventExpress site')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_unauthorized_user(self):
        response_decoded_json = requests.post(URL_AUTH['url_login'], data=json.dumps(AUTH_PAYLOADS['payload_unauth']),
                                              headers=HEADER['header'])
        mes = response_decoded_json.json()
        assert 400 == response_decoded_json.status_code, "You have BAD REQUEST"
        assert "User not found" == mes, "There is unexpected ability to login as unknown user"

    @allure.feature("Register new user api")
    @allure.story('User that is previously registered does not have an ability to register in EventExpress site')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_already_exist(self):
        response_decoded_json = requests.post(URL_AUTH['url_register'],
                                              data=json.dumps(AUTH_PAYLOADS['payload_user']),
                                              headers=HEADER['header'])
        mes = response_decoded_json.json()
        assert "Email already exists in database" == mes, "There is no verification of existing email on register"
        assert 400 == response_decoded_json.status_code, "You have BAD REQUEST"

    @allure.feature("Register new user api")
    @allure.story('Every new user have an ability to register in EventExpress site')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_new_user(self):
        response_decoded_json = requests.post(URL_AUTH['url_register'],
                                              data=json.dumps(AUTH_PAYLOADS['payload_unauth']),
                                              headers=HEADER['header'])
        assert 200 == response_decoded_json.status_code

    @pytest.mark.skip("there is no correct way to verify using response or db that password changed")
    def test_change_password(self):
        response_decoded_json = requests.post(URL_AUTH['url_change_password'],
                                              data=json.dumps(AUTH_PAYLOADS['payload_change_password']),
                                              headers=self['header'])
        assert 200 == response_decoded_json.status_code
