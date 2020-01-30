import os
import json
import requests
from tests_api.config import URL_AUTH, AUTH_PAYLOADS, HEADER, URL_USERS, URL_EVENT


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
            URL_AUTH['url_login'], data=json.dumps(
                AUTH_PAYLOADS['payload_user']), headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {
            "accept": "application/json",
            "Content-Type": "application/json-patch+json",
            "authorization": "Bearer " + auth}
        return header

    def get_header_auth_vasya(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login'], data=json.dumps(
                AUTH_PAYLOADS['payload_vasya']), headers=HEADER['header'])
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


class Event():

    CURRENT_PATH = os.path.abspath('CH_096_TAQC')

    header = {
        'Content-Type': 'multipart/form-data',
        'Authorization': Header().get_token_admin()
    }

    payload = {
        'Title': 'Test Event',
        'Description': 'Event for testing search',
        'DateFrom': 'Fra Jan 24 2020',
        'DateTo': 'Mon Feb 10 2020',
        'User.Id': 'f320932e-aac2-4999-32d3-08d79b47df59',
        'CityId': '418ad80a-85da-4033-f8df-08d79b47df2b',
        'Categories[0].Id': '60c56914-a974-4b4c-f461-08d79b47df60'
    }

    files = {
        # 'Photo': open(os.path.join(CURRENT_PATH) + 'Data\\imageAddEvent\\testing_img.png','rb')
    }

    def create(self):
        response = requests.post(
            URL_EVENT['url_event_edit'],
            headers=self.header,
            data=self.payload,
            files=self.files)
        print(
            URL_EVENT['url_event_edit'],
            self.header,
            self.payload,
            self.files)
        print(response)

    def get_token_admin(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login'], data=json.dumps(
                AUTH_PAYLOADS['payload_admin']), headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        token = "Bearer " + auth
        return token


class User:
    """Class to test Users API"""

    def __init__(
            self,
            id="e02dfd94-a8a9-4b1a-6cfc-08d7a28d1878",
            name='Vasya',
            gender=0,
            birthday="2000-01-01"):
        """Init new user data"""
        self.id = id
        self.name = name
        self.birthday = str(birthday) + "T00:00:00"
        self.gender = gender
        self.payload_edit_gender = {
            "id": self.id,
            "gender": self.gender}
        self.payload_edit_birthday = {
            "id": self.id,
            "birthday": self.birthday}
        self.payload_edit_username = {
            "id": self.id,
            "name": self.name}

    def PAYLOAD_edit_gender(self):
        """Reload PAYLOAD_gender data"""
        PAYLOAD_edit_gender = {
            "id": self.id,
            "gender": self.gender}
        return PAYLOAD_edit_gender

    def PAYLOAD_edit_username(self):
        """Reload PAYLOAD_username data"""
        PAYLOAD_edit_username = {
            "id": self.id,
            "name": self.name}
        return PAYLOAD_edit_username

    def PAYLOAD_edit_birthday(self):
        """Reload PAYLOAD_birthday data"""
        PAYLOAD_edit_birthday = {
            "id": self.id,
            "birthday": self.birthday}
        return PAYLOAD_edit_birthday

    def edit_gender(self, gender):
        """Edit user gender"""
        self.gender = gender
        response_decoded_json = requests.post(
            URL_USERS['edit_gender'],
            data=json.dumps(
                self.PAYLOAD_edit_gender()),
            headers=Header().get_header_auth_vasya())
        print("Гендер змінено")

    def edit_username(self, username):
        """Edit user name"""
        self.name = username
        response_decoded_json = requests.post(
            URL_USERS['edit_username'],
            data=json.dumps(
                self.PAYLOAD_edit_username()),
            headers=Header().get_header_auth_vasya())
        print("Ім'я змінено")
        return response_decoded_json

    def edit_birthday(self, birthday):
        """Edit user birthday"""
        self.birthday = birthday
        response_decoded_json = requests.post(
            URL_USERS['edit_birthday'],
            data=json.dumps(
                self.PAYLOAD_edit_birthday()),
            headers=Header().get_header_auth_vasya())
        print("Дату відредаговано на ", self.birthday[:10])
        return response_decoded_json

    def set_attitude(self, id, attitude):
        """Set attitude to User from Vasya"""
        response_decoded_json = requests.post(
            URL_USERS['set_attitude'],
            data=json.dumps({
                "userFromId": self.id,
                "userToId": id,
                "attitude": attitude
            }),
            headers=Header().get_header_auth_vasya())
        return response_decoded_json

    def back_attitude(self, id):
        """Set attitude to User from Vasya"""
        response_decoded_json = requests.post(
            URL_USERS['set_attitude'],
            data=json.dumps({
                "userFromId": self.id,
                "userToId": id,
                "attitude": 2
            }),
            headers=Header().get_header_auth_vasya())
        return response_decoded_json

    def get_info_by_id(self):
        """Get all user info by user-id"""
        url = URL_USERS['user_by_id'] + self.id
        response_decoded_json = requests.get(
            url,
            headers=Header().get_header_auth_vasya())
        Json = response_decoded_json.content.decode()
        dictionary = json.loads(Json)
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

    def get_username(self):
        """Get user username"""
        dictionary = self.get_info_by_id()
        birthday = dictionary["name"]
        return birthday


"""
id = "e02dfd94-a8a9-4b1a-6cfc-08d7a28d1878"
print(Header().get_token_admin())
user = User(id, "Jesus", 2, "2001-06-04")
print(user.get_info_by_id())
user.edit_username()
user.edit_gender()
user.edit_birthday()
print(user.get_info_by_id())
user.back_username()
user.back_gender()
user.back_birthday()
print(user.get_info_by_id())
"""


class User1:
    """Class to test User API"""

    def __init__(self, name):
        """Init new user data"""
        self.id = None  # "id": "a1d49d6a-f832-4f2a-32d4-08d79b47df59"
        self.name = name  # UserTest
        self.header = Header().get_header_auth_admin()

    def block(self):
        """
        Block user by name
        :param: username :type: str
        :param: header :type: instance of Header()
        :return: instance of response object
        """
        self.get_user_id()
        payload_block_user = {"id": self.id}
        print('***********', payload_block_user)
        response = requests.post(
            URL_USERS['url_block_user'],
            data=json.dumps(
                payload_block_user),
            headers=self.header)
        print(f"User {self.name} has blocked")
        return response

    def unblock(self):
        """Unblock user by name
        :param: username :type: str
        :param: header :type: instance of Header()
        :return: instance of response object
        """
        self.get_user_id()
        payload_block_user = {"id": self.id}
        print('------------', payload_block_user)

        response = requests.post(
            URL_USERS['url_unblock_user'],
            data=json.dumps(
                payload_block_user),
            headers=self.header)
        print(f"User {self.name} has unblocked")
        return response

    def get_user_id(self):
        """
        API test. This method search a user by id
        :param: username
        :type: str
        :param: header
        :type: str
        :return: user id
        :type: str
        """
        response = requests.get(URL_USERS['url_search_users'],
                                headers=self.header)
        resp = response.json()
        users_count = len(resp['items'])

        for index in range(users_count):
            if resp['items'][index]['username'] == self.name:
                self.id = resp['items'][index]['id']
                print('=========', self.id)
        return self.id

    def collect_users(self, response):
        """
        API test. This method search all users
        :param: header :type: instance of Header()
        :return: list of all users
        :type: list of str
        """

        resp = response.json()
        users_count = len(resp['items'])

        users = []
        for index in range(users_count):
            users.append(resp['items'][index]['username'])

        return users


#name = 'UserTest'
#user = User1(name)
# print(user.block())
# print(user.unblock())
