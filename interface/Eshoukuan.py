# coding=utf-8
import base64,hashlib,json
from Crypto.Cipher import AES
import requests
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from binascii import b2a_hex, a2b_hex
from collections import OrderedDict

private_key='''MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAMtrfcrKrG41tG5aWNKJusCs9yVkdt4G5/Vg7QaRsSZiWOxsd/zs/aNuS9SuzL/YMrqYCRoil12nhqhxQDoQdncUIRwrc+HhjtshE9btMVJFWyFkUbaBA0DsPwMzGsVxhOByBKimoDjCL2I92fawv0IAJDhpd46kly0TGLf8DcbNAgMBAAECgYB+cX2KrXqLMwTJx40IqaYVGC6z5oPgtQhARZRwDeXAx0chBrd611E94lRuio0o/tlhlRmrTi8qfvS8BVF4Bj2r39Le3/wdzcVDoK8ruVRUW+S9JI+9p3WNVwIvderROg7ttcl67XV5jRYQqOsqDZa9f224luN0B4q41yzz2c2KAQJBAP5A2uQrmnY9mOkeCU6mveQpneP6c8w0rXIXFEyFKD3t/MjREb17/GRhSu/ZSXnzKW5F8C+d5dqXAFETBfH7k4ECQQDM0TzUg4i+i4xsQ9NPRZzBT1HI998DI2umjPfEYLGdCZvsEhV4B4rCKpVsNKdNWkNgdd6sKOj53n0yTBwjIulNAkEAilYrQv5eenslWaFYGw0qQJxMJiC9JJx8ypi4GLJSpO96HKF0b46oUs2FAl9NVSbyoec3uhDFYVvLdlFNaM4jAQJAULo71qtNb4UDQPzuwbT3Vv4ThzmjjdIdMRUo5x8RgoryCPcLvTaDy4oLQQ3zzzo/ijqLHKI3SZ0XDYcQJA0zlQJBAJvVdpJy8472UZvHXrrjG7//ohyiTNbYKLRU7mDtH1e2uQz+BI+lha4LlZaN3jFUssV1FnG0C7otaOKsF7s302Y='''
public_key="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDLa33KyqxuNbRuWljSibrArPclZHbeBuf1YO0GkbEmYljsbHf87P2jbkvUrsy/2DK6mAkaIpddp4aocUA6EHZ3FCEcK3Ph4Y7bIRPW7TFSRVshZFG2gQNA7D8DMxrFcYTgcgSopqA4wi9iPdn2sL9CACQ4aXeOpJctExi3/A3GzQIDAQAB"
priKey = '''-----BEGIN RSA PRIVATE KEY-----
MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAMtrfcrKrG41tG5aWNKJusCs9yVkdt4G5/Vg7QaRsSZiWOxsd/zs/aNuS9SuzL/YMrqYCRoil12nhqhxQDoQdncUIRwrc+HhjtshE9btMVJFWyFkUbaBA0DsPwMzGsVxhOByBKimoDjCL2I92fawv0IAJDhpd46kly0TGLf8DcbNAgMBAAECgYB+cX2KrXqLMwTJx40IqaYVGC6z5oPgtQhARZRwDeXAx0chBrd611E94lRuio0o/tlhlRmrTi8qfvS8BVF4Bj2r39Le3/wdzcVDoK8ruVRUW+S9JI+9p3WNVwIvderROg7ttcl67XV5jRYQqOsqDZa9f224luN0B4q41yzz2c2KAQJBAP5A2uQrmnY9mOkeCU6mveQpneP6c8w0rXIXFEyFKD3t/MjREb17/GRhSu/ZSXnzKW5F8C+d5dqXAFETBfH7k4ECQQDM0TzUg4i+i4xsQ9NPRZzBT1HI998DI2umjPfEYLGdCZvsEhV4B4rCKpVsNKdNWkNgdd6sKOj53n0yTBwjIulNAkEAilYrQv5eenslWaFYGw0qQJxMJiC9JJx8ypi4GLJSpO96HKF0b46oUs2FAl9NVSbyoec3uhDFYVvLdlFNaM4jAQJAULo71qtNb4UDQPzuwbT3Vv4ThzmjjdIdMRUo5x8RgoryCPcLvTaDy4oLQQ3zzzo/ijqLHKI3SZ0XDYcQJA0zlQJBAJvVdpJy8472UZvHXrrjG7//ohyiTNbYKLRU7mDtH1e2uQz+BI+lha4LlZaN3jFUssV1FnG0C7otaOKsF7s302Y=
-----END RSA PRIVATE KEY-----'''
AES_Key="2e8a490fd9745a68d1930aabcacb3a6a"

url = "https://merchant.ardy0220.top/out/addItems"

def paixu(sha_data):
    sha_data = sorted(sha_data.items())
    param = []
    for _key, _value in sha_data:
        param.append(_key + "=" + _value)
    print (('&'.join(param).encode()))
    return ('&'.join(param).encode())
def sign(date, prikey):
    key = RSA.import_key(prikey)
    h = SHA.new(paixu(date))
    print (h.hexdigest())
    signer = PKCS1_v1_5.new(key)
    sign_auter = signer.sign(h)
    return str(b2a_hex(sign_auter),'utf-8')
def encrypt_oracle(text):
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    text = json.dumps(text,separators=(',',':'))
    key = b'2e8a490fd9745a68d1930aabcacb3a6a'
    aes = AES.new(key, AES.MODE_ECB)
    encrypted_text = b2a_hex(aes.encrypt(bytes(pad(text),'utf-8')))
    return str(encrypted_text,'utf-8')

def login(url,data):
    r = requests.post(url,data=data)
    result = r.json()
    return result


if __name__ == '__main__':
    payload = OrderedDict([("paymentCode","1000000477581663"),
                           ("merchantId","20160000"),
                           ("list","[{\"cashierId\":\"213639\",\"payAmt\":10,\"scode\":\"1000000458046259\"}]")
                           ])
    data = {"paymentCode": "1000000477581663",
               "merchantId": "20160000",
               "list": "[{\"cashierId\":\"213639\",\"payAmt\":10,\"scode\":\"1000000458046259\"}]"}
    sign1 = sign(payload,priKey)
    print (sign1)
    aes_data = encrypt_oracle(payload)
    print (aes_data)
    data1 = {"data":aes_data,"sign":sign1}
    result = login(url,data=data1)
    print (result)

