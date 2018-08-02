from Crypto.Cipher import AES
import base64
import requests,unittest,json

class AESTest(unittest.TestCase):

    def setUp(self):
        BS = 16
        self.pad = lambda s :s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        self.base_url = "http://127.0.0.1:8000/api/sec_get_guest_list/"
        self.app_key = b'W7v4D60fds2Cmk2U'

    def encryptBase64(self,src):
        return base64.b64encode(src)


    def encryptAES(self,src,key):
        '''生成AES密文'''
        iv = b'1172311105789011'
        cryptor = AES.new(key,AES.MODE_CBC,iv)
        print (src,type(src),self.pad(src))
        ciphertext = cryptor.encrypt(self.pad(src).encode())
        return self.encryptBase64(ciphertext)

    def test_ase_interface(self):
        'test ase interface'
        pyaload = {'eid':1,'phone':'13511001101'}
        # 加密
        encoded = self.encryptAES(json.dumps(pyaload),self.app_key)
        print (encoded,type(encoded))
        r = requests.post(self.base_url,data={'data':encoded})
        result = r.json()
        print (result)
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')

    def test_ase_interface_phone_unll(self):
        '客户电话号码为空'
        pyaload = {'eid':1,'phone':''}
        # 加密
        encoded = self.encryptAES(json.dumps(pyaload),self.app_key)
        print (encoded,type(encoded))
        r = requests.post(self.base_url,data={'data':encoded})
        result = r.json()
        print (result)
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')

if __name__ == '__main__':
    unittest.main()