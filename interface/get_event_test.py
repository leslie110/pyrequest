# conding=utf-8
from db_fixture.test_data import init_data
import requests
import unittest

class GetEventTest(unittest.TestCase):
    '''查询发布会'''
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    def test_all_null(self):
        '''数据为空'''
        payload = {'eid':'','name':''}
        self.result = requests.get(self.url,params=payload)
        r = self.result.json()
        self.assertEqual(r['status'],10021)
        self.assertEqual(r['message'],'parameter error')

    def test_eid_unll(self):
        '''eid为空'''
        payload = {'eid': '', 'name': '红米1'}
        self.result = requests.get(self.url, params=payload)
        r = self.result.json()
        self.assertEqual(r['status'], 200)
        self.assertEqual(r['message'], 'success')

    def test_name_unll(self):
        '''name为空'''
        payload = {'eid': '1', 'name': ''}
        self.result = requests.get(self.url, params=payload)
        r = self.result.json()
        self.assertEqual(r['status'], 200)
        self.assertEqual(r['message'], 'success')

    def test_id_error(self):
        '''id不存在'''
        payload = {'eid': 1000, 'name': ''}
        self.result = requests.get(self.url, params=payload)
        r = self.result.json()
        self.assertEqual(r['status'], 10022)
        self.assertEqual(r['message'], 'query result is empty')

    def test_name_error(self):
        '''name不存在'''
        payload = {'eid':'', 'name': '!@#'}
        self.result = requests.get(self.url, params=payload)
        r = self.result.json()
        self.assertEqual(r['status'], 10022)
        self.assertEqual(r['message'], 'query result is empty')

    def tearDown(self):
        print (self.result)

if __name__ == '__main__':
    init_data()
    unittest.main()

