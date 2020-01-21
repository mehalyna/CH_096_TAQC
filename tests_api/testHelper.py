import json
import requests
from tests_api.config import URL_AUTH, AUTH_PAYLOADS, HEADER


class Header:

    def get_header_auth_admin(self):
        response_decoded_json = requests.post(URL_AUTH.url_login, data=json.dumps(AUTH_PAYLOADS.payload_admin),
                                              headers=HEADER.header)
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json",
                  "authorization": "Bearer " + auth}
        return header

    def get_header_auth_user(self):
        response_decoded_json = requests.post(URL_AUTH.url_login, data=json.dumps(AUTH_PAYLOADS.payload_user),
                                              headers=HEADER.header)
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json",
                  "authorization": "Bearer " + auth}
        return header
