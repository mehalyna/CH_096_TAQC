import json

import requests


class UrlAuth:
    url_login = "http://34.65.101.58:5002/api/Authentication/Login"
    url_register = "http://34.65.101.58:5002/api/Authentication/Register"
    url_login_fb = "http://34.65.101.58:5002/api/Authentication/FacebookLogin"
    url_login_google = "http://34.65.101.58:5002/api/Authentication/google"


class UrlCategory:
    url_category_edit = "http://34.65.101.58:5002/api/Category/Edit"
    url_category_all = "http://34.65.101.58:5002/api/Category/All"
    url_category_delete = "http://34.65.101.58:5002/api/Category/Delete/"


class AuthPayloads:
    payload_admin = {"Email": "admin@gmail.com", "Password": "1qaz1qaz"}
    payload_user = {"Email": "user@gmail.com", "Password": "1qaz1qaz"}
    payload_unauth = {"Email": "katya@gmail.com", "Password": "123"}

class CategoryPayloads:
    category_to_edit = {"Id": "F535A1D6-EEC4-4697-B4AD-08D7858FCA63", "Name": "MountNew"}
    category_to_create = {"Name": "new"}

class Header:
    header = {"accept": "application/json", "Content-Type": "application/json-patch+json"}

    def get_header_auth_admin(self):
        response_decoded_json = requests.post(UrlAuth.url_login, data=json.dumps(AuthPayloads.payload_admin),
                                              headers=Header.header)
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json",
                  "authorization": "Bearer " + auth}
        return header

    def get_header_auth_user(self):
        response_decoded_json = requests.post(UrlAuth.url_login, data=json.dumps(AuthPayloads.payload_user),
                                              headers=Header.header)
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json",
                  "authorization": "Bearer " + auth}
        return header
