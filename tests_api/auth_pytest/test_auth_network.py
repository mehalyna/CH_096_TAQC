"""
Api tests for login through social network
"""
import json
import requests
import allure
from tests_api.config import URL_AUTH, HEADER, AUTH_PAYLOADS


class TestAuth:
    """
    Testcases for checking login through social network
    """

    @allure.link(
        "http://34.65.101.58:5002",
        name='Main page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_as_user_with_facebook(self):
        """
        Test for login as user with Facebook
        """
        response_decoded_json = requests.post(
            URL_AUTH['url_login_fb'], data=json.dumps(
                AUTH_PAYLOADS['payload_user']), headers=HEADER['header'])
        resp = response_decoded_json.json()
        name = "UserTest"
        role = "User"
        assert name == resp["name"], f"You don't login with correct name {name}"
        assert role == resp["role"], f"You don't login with correct role {role}"
        assert response_decoded_json.status_code == 200, "You have BAD REQUEST"

    def test_login_as_admin_with_facebook(self):
        """
        Test for login as admin with Facebook
        """
        response_decoded_json = requests.post(
            URL_AUTH['url_login_fb'], data=json.dumps(
                AUTH_PAYLOADS['payload_admin']), headers=HEADER['header'])
        resp = response_decoded_json.json()
        info = "Admin"
        assert info == resp["name"], f"You don't login with correct name {info}"
        assert info == resp["role"], f"You don't login with correct role {info}"
        assert response_decoded_json.status_code == 200, "You have BAD REQUEST"

    def test_login_as_admin_with_google(self):
        """
        Test for login as admin with Google
        """
        response_decoded_json = requests.post(
            URL_AUTH['url_login_google'], data=json.dumps(
                AUTH_PAYLOADS['payload_admin']), headers=HEADER['header'])
        assert response_decoded_json.status_code == 400

    def test_login_as_user_with_google(self):
        """
        Test for login as user with Google
        """
        response_decoded_json = requests.post(
            URL_AUTH['url_login_google'], data=json.dumps(
                AUTH_PAYLOADS['payload_user']), headers=HEADER['header'])
        assert response_decoded_json.status_code == 400
