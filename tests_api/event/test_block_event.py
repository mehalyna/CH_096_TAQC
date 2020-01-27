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
        print("event")

    def test_block_event(self):
        response=requests.get(URL_EVENT['get_all_event']+EVENT_PAYLOAD['blocked']+EVENT_PAYLOAD['page'], headers=self.header)
        resp1 = response.json()
        id_event_after = resp1['items']['id']
        response = requests.post(URL_EVENT['block_event']+EVENT_PAYLOAD['eventId']+str(db.get_id_event_by_name('Test Event')), headers=self.header_admin)
        resp2 = response.json()
        id_event_before = resp['items']['id']
        self.assertNotEqual(resp1, resp2, "Event is blocked!")

    @classmethod
    def tearDownClass(cls):
        db.delete_category_with_name('Test Event')

if __name__ == '__main__':
    unittest.main()
    