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
        r = [i['name'] for i in response_decoded_json.json()]
        self.assertIn('Sea', r)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_category_edit_mount(self):
        response_decoded_json = requests.post(
            URL_CATEGORY['url_category_edit'], data=json.dumps(
                CATEGORY_PAYLOADS['category_to_edit']), headers=self.header)
        id = self.conn.get_name_of_category_using_id(CATEGORY_PAYLOADS['category_to_edit']['Id'])
        self.assertEqual(id, CATEGORY_PAYLOADS['category_to_edit']['Name'])
        self.assertEqual(200, response_decoded_json.status_code)

    def test_create_category(self):
        response_decoded_json = requests.post(
            URL_CATEGORY['url_category_edit'], data=json.dumps(
                CATEGORY_PAYLOADS['category_to_create']), headers=self.header)
        id = self.conn.get_id_using_name(CATEGORY_PAYLOADS['category_to_create']['Name'])
        self.assertIsNotNone(id)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_delete_category(self):
        id = self.conn.get_id_using_name("category to be deleted")
        response_decoded_json = requests.post(
            URL_CATEGORY['url_category_delete'] +
            id, headers=self.header)
        self.assertEqual(str(0), self.conn.get_count_of_category_on_name("category to be deleted"))
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
