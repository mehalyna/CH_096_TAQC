import json
import unittest
import requests
from tests_api.testHelper import Header
from tests_api.config import URL_CATEGORY, CATEGORY_PAYLOADS
from dbconnection import Connection


class testCategoryAdminSide(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.header = Header().get_header_auth_admin()
        cls.conn = Connection()
        cls.conn.create_category_with_name("category to be deleted")

    def test_category_get_all(self):
        response_decoded_json = requests.get(
            URL_CATEGORY['url_category_all'], headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_category_edit_sea(self):
        response_decoded_json = requests.post(
            URL_CATEGORY['url_category_edit'], data=json.dumps(
                CATEGORY_PAYLOADS['category_to_edit']), headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_create_category(self):
        response_decoded_json = requests.post(
            URL_CATEGORY['url_category_edit'], data=json.dumps(
                CATEGORY_PAYLOADS['category_to_create']), headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_delete_category(self):
        id = self.conn.get_id_using_name("category to be deleted")
        response_decoded_json = requests.post(
            URL_CATEGORY['url_category_delete'] +
            id, headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    @classmethod
    def tearDownClass(cls):
        cls.conn = Connection()
        cls.conn.delete_category_with_name("new")
        cls.conn.delete_category_with_name("category to be deleted")
        cls.conn.edit_category_with_name("MountNew", "Mount")
        cls.conn.close()


if __name__ == '__main__':
    unittest.main()
