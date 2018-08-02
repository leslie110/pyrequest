# conding=utf-8

import requests
import unittest
from db_fixture.test_data import init_data

class AddGuestTest(unittest.TestCase):
    '''添加嘉宾接口测试'''
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/add_guest/"

    def test_all_null(self):
        '''所有数据为空'''
        payload = {'eid':'','realname':'','phone':'','email':''}
        self.result = requests.post(self.url,data=payload)
        r = self.result.json()
        self.assertEqual(r['status'],10021)
        self.assertEqual(r['message'],'parameter error')

    def test_eid_exist(self):
        '''eid存在'''
        payload = {'eid':1,'realname':'alen4','phone':15309210000,'email':'alen4@mail.com'}
        self.result = requests.post(self.url,data=payload)
        r = self.result.json()
        self.assertEqual(r['status'],10021)
        self.assertEqual(r['message'],'parameter error')

if __name__ == '__main__':
    unittest.main()
