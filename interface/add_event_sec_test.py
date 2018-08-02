# conding=utf-8

import unittest,requests,hashlib
import time
from Crypto.Cipher import AES



class AddEventSecTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/sec_add_event/"
        # app_key
        self.api_key = "庾林云"
        # 当前时间
        now_time = time.time()
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.client_time = str(now_time).split('.')[0]
        # sign 签名
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()

    def test_add_event_request_error(self):
        '''请求方法错误'''
        r = requests.get(self.url)
        result = r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'request error')

    def test_add_event_sign_null(self):
       '''签名参数为空'''
       payload = {'eid':'','limit':'','address':'','start_time':'','time':'','sign':''}
       r = requests.post(self.url,data=payload)
       result = r.json()
       self.assertEqual(result['status'],10012)
       self.assertEqual(result['message'],'user sign null')

    def test_add_event_time_out(self):
        '''请求超时'''
        now_time = str(int(self.client_time) - 61)
        payload = {'eid': 1, 'limit': '', 'address': '', 'start_time': '', 'time': now_time, 'sign':'abc'}
        r = requests.post(self.url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10013)
        self.assertEqual(result['message'], 'user sign timeout')

    def test_add_event_sign_error(self):
        '''签名错误'''
        payload = {'eid': 1, 'limit': '', 'address': '', 'start_time': '', 'time': self.client_time, 'sign': 'abc'}
        r = requests.post(self.url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10014)
        self.assertEqual(result['message'], 'user sign error')

    def test_add_event_success(self):
        '''添加成功'''
        payload = {'eid':23,'name':'7月手机发布3','limit': 2000, 'address':'深圳宝体', 'start_time': self.start_time, 'time': self.client_time, 'sign':self.sign_md5}
        r = requests.post(self.url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'add event success')

    def tearDown(self):
        print(self.start_time)
        print (self.sign_md5)



if __name__ == '__main__':
    unittest.main()









