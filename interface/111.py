# conding=uft-8
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA as rsa
import hashlib,base64,json
from itsdangerous import base64_encode, base64_decode


obj = AES.new(b'2e8a490fd9745a68d1930aabcacb3a6a',AES.MODE_CBC,b'this is an IV456')
PADDING = '\0'
pan = lambda s :s + (16 - len(s) % 16) * PADDING
message = "abcd"
ciphertext = obj.encrypt((pan(message)))
data = base64_decode(ciphertext)
print (data)
# obj2 = AES.new(b'this is a key123',AES.MODE_CBC,b'this is an IV456')
# message1 = obj2.decrypt(base64.b64decode(data))
# print (message1)

a = sorted('hdsfkdhggh')
print (a)
md5 = hashlib.md5()
md5.update(''.join(a).encode('utf-8'))
print (''.join(a).encode('utf-8'))
sign_md5 = md5.hexdigest()
print (sign_md5)
sha1 = hashlib.sha1()
sha1.update(''.join(a).encode('utf-8'))
print (sha1.hexdigest())

text = sorted("retre4!@")
aa = ''.join(text)
print (aa)

text_md5 = hashlib.md5(aa.encode('utf-8'))
print (text_md5.digest())

text_sha1 = hashlib.sha1(aa.encode('utf-8'))
print(text_sha1.hexdigest())

# 或者采用如下的方式进行散列
m = hashlib.md5()
m.update(''.join(a).encode('utf-8'))
m.hexdigest()
print (m.hexdigest())

a = {'id':1,'phone':'15821458745'}
b = json.dumps(a)
print (b,type(b))
