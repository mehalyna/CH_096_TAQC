import json
import requests
import os


class UrlAuth:
    url_login = "http://34.65.101.58:5002/api/Authentication/Login"
    url_register = "http://34.65.101.58:5002/api/Authentication/Register"
    url_login_fb = "http://localhost:49862/api/Authentication/FacebookLogin"
    url_login_google = "http://34.65.101.58:5002/api/Authentication/google"


class UrlCategory:
    url_category_edit = "http://34.65.101.58:5002/api/Category/Edit"
    url_category_all = "http://34.65.101.58:5002/api/Category/All"
    url_category_delete = "http://34.65.101.58:5002/api/Category/Delete/"

class UrlEvent:
    url_event_edit = "http://34.65.101.58:5002/api/Event/Edit/"
    #url_event_edit = "http://localhost:49862/api/Event/Edit/"

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
    
    def get_token_admin(self):
        response_decoded_json = requests.post(UrlAuth.url_login, data=json.dumps(AuthPayloads.payload_admin),
                                              headers=Header.header)
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
        'Photo': open(os.path.join(CURRENT_PATH) + '\\Data\\imageAddEvent\\testing_img.png','rb')
        }

    def create(self):
        response = requests.post(UrlEvent.url_event_edit, headers=self.header, data = self.payload, files = self.files)
        print(UrlEvent.url_event_edit, self.header, self.payload, self.files)
        print(response)


