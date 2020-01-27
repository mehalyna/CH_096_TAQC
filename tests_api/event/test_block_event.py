import unittest
import requests
from tests_api.config import URL_EVENT, EVENT_PAYLOAD
from tests_api.testHelper import Header
from dbconnection import Connection as db


class TestChat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.header_user = Header().get_header_auth_user()
        cls.header_admin = Header().get_header_auth_admin()
        db.create_event()

    def test_get_chat_user(self):
        response = requests.post(URL_EVENT['block_event']+EVENT_PAYLOAD['eventId']+str(db.get_id_event_by_name('Test Event')), headers=self.header_admin)
        resp = response.status_code
        print(response)
        #self.assertEqual(200, resp, "You have BAD REQUEST")

if __name__ == '__main__':
    unittest.main()
    