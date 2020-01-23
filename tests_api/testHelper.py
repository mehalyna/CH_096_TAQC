import json
import requests
from tests_api.config import URL_AUTH, AUTH_PAYLOADS, HEADER, URL_USERS, USER_PAYLOADS


class Header:

    def get_header_auth_admin(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login'], data=json.dumps(
                AUTH_PAYLOADS['payload_admin']), headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {
            "accept": "application/json",
            "Content-Type": "application/json-patch+json",
            "authorization": "Bearer " + auth}
        return header

    def get_header_auth_user(self):
        response_decoded_json = requests.post(
            URL_AUTH.url_login, data=json.dumps(
                AUTH_PAYLOADS.payload_user), headers=HEADER.header)
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {
            "accept": "application/json",
            "Content-Type": "application/json-patch+json",
            "authorization": "Bearer " + auth}
        return header

    def get_token_admin(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login'], data=json.dumps(
                AUTH_PAYLOADS['payload_admin']), headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        token = "Bearer " + auth
        return token

    def admin_header(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login'], data=json.dumps(
                AUTH_PAYLOADS['payload_admin']), headers={
                "accept": "application/json"})
        h = json.loads(response_decoded_json.content.decode())
        auth = self.get_token_admin()
        header = {"Content-Type": "application/json",
                  "authorization": auth}
        return header


class User:
    """Class to test Users API"""

    def __init__(
            self,
            id="f320932e-aac2-4999-32d3-08d79b47df59",
            gender=0,
            birthday="2000-01-01"):
        """Init new user data"""
        self.id = id
        self.birthday = birthday + "T00:00:00"
        self.gender = gender
        self.payload_edit_gender = {
            "id": self.id,
            "gender": self.gender}
        self.payload_edit_birthday = {
            "id": self.id,
            "birthday": self.birthday}

    def PAYLOAD_edit_gender(self):
        """Reload PAYLOAD_gender data"""
        PAYLOAD_edit_gender = {
            "id": self.id,
            "gender": self.gender}
        return PAYLOAD_edit_gender

    def PAYLOAD_edit_birthday(self):
        """Reload PAYLOAD_birthday data"""
        PAYLOAD_edit_birthday = {
            "id": self.id,
            "birthday": self.birthday}
        return PAYLOAD_edit_birthday

    def edit_gender(self):
        """Edit user gender"""
        response_decoded_json = requests.post(
            URL_USERS['edit_gender'],
            data=json.dumps(
                self.payload_edit_gender),
            headers=Header().get_header_auth_admin())
        print("Гендер змінено")

    def edit_birthday(self):
        """Edit user birthday"""
        response_decoded_json = requests.post(
            URL_USERS['edit_birthday'],
            data=json.dumps(
                self.payload_edit_birthday),
            headers=Header().get_header_auth_admin())
        print("Дату відредаговано на ", self.birthday[:10])

    def back_gender(self):
        """Return user data"""
        self.gender = 0
        response_decoded_json = requests.post(
            URL_USERS['edit_gender'],
            data=json.dumps(
                self.PAYLOAD_edit_gender()),
            headers=Header().get_header_auth_admin())
        print("Гендер вернувся")

    def back_birthday(self):
        """Return user birthday"""
        self.birthday = "2000-01-01T00:00:00"
        response_decoded_json = requests.post(
            URL_USERS['edit_gender'],
            data=json.dumps(
                self.PAYLOAD_edit_birthday()),
            headers=Header().get_header_auth_admin())
        print("Дату повернено на ", self.birthday[:10])

    def get_info_by_id(self):
        """Get all user info by user-id"""
        response_decoded_json = requests.get(
            URL_USERS['user_by_id_admin'],
            headers=Header().get_header_auth_admin())
        Json = response_decoded_json.content.decode()
        dictionary = json.loads(Json)
        # print(dictionary)
        return dictionary

    def get_gender(self):
        """Get user gender"""
        dictionary = self.get_info_by_id()
        gender = dictionary["gender"]
        return gender

    def get_birthday(self):
        """Get user birthday"""
        dictionary = self.get_info_by_id()
        birthday = dictionary["birthday"]
        return birthday[:10]


id = "f320932e-aac2-4999-32d3-08d79b47df59"
print(Header().get_token_admin())
user = User(id, 1, "2001-06-04")
user.edit_birthday()
# print(user.get_info_by_id())
print(user.get_birthday())
user.back_birthday()
# print(user.get_info_by_id())
print(user.get_birthday())
user.edit_gender()
# print(user.get_info_by_id())
print(user.get_gender())
user.back_gender()
# print(user.get_info_by_id())
print(user.get_gender())
