import os
import json
import requests
from tests_api.config import URL_AUTH, AUTH_PAYLOADS, HEADER


class Header:

    def get_header_auth_admin(self):
        response_decoded_json = requests.post(URL_AUTH.url_login, data=json.dumps(AUTH_PAYLOADS.payload_admin),
                                              headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json",
                  "authorization": "Bearer " + auth}
        return header

    def get_header_auth_user(self):
        response_decoded_json = requests.post(URL_AUTH.url_login, data=json.dumps(AUTH_PAYLOADS.payload_user),
                                              headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json",
                  "authorization": "Bearer " + auth}
        return header
    
    def get_token_admin(self):
        response_decoded_json = requests.post(URL_AUTH['url_login'], data=json.dumps(AUTH_PAYLOADS['payload_admin']),
                                              headers=HEADER['header'])
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
        response = requests.post(URL_EVENT['url_event_edit'], headers=self.header, data = self.payload, files = self.files)
        print(UrlEvent.url_event_edit, self.header, self.payload, self.files)
        print(response)


