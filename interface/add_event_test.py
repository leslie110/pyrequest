# coding=utf-8
import unittest
import requests
import os,sys,time
from db_fixture import test_data

class AddEventTest(unittest.TestCase):
    '''添加发布会'''
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/add_event/"
        self.time_at = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

    def tearDown(self):
        print (self.result)

    def test_add_event_all_null(self):
        '''所有参数为空'''
        payload = {'eid':'','name':'','limit':'','address':'','status':'','start_time':''}
        r = requests.post(self.url,data=payload)
        self.result = r.json()
        print (self.result)
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error')

    def test_add_event_eid_exist(self):
        '''id已经存在'''
        payload = {'eid':'1','name':'一家发布会','limit':'2000','status':0,'address':'深圳宝体','start_time':self.time_at}
        r = requests.post(self.url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10022)
        self.assertEqual(self.result['message'],'event_id already exists')

    def test_add_event_name_exist(self):
        '''name已经存在'''
        payload = {'eid':6, 'name': '红米1', 'limit': '2000','status':1,'address': '深圳宝体', 'start_time': self.time_at}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        '''日期格式错误'''
        payload = {'eid': 6, 'name': '红米999', 'limit': '2000','status':0, 'address': '深圳宝体', 'start_time': time.localtime()}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], 'start_time format error. is must be in YYYY-MM-DD HH:MM:SS format.')

    def test_add_event_success(self):
        '''添加成功'''
        payload = {'eid':6, 'name': '红米999', 'limit': '2000','status':0, 'address': '深圳宝体', 'start_time': self.time_at}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')



if __name__ == '__main__':
    test_data.init_data()   #初始化接口测试数据
    unittest.main()

