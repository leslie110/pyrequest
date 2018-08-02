# coding=utf-8
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
import base64
from binascii import b2a_hex,a2b_hex


def paixu(sha_data):
    # 将字典进行排序并转成&字符串格式
    sha_data = sorted(sha_data.items())
    param = []
    for _key, _value in sha_data:
        param.append(_key + "=" + _value)
    return ('&'.join(param).encode())

def sign(date, prikey):

    key = RSA.import_key(prikey)
    h = SHA.new(paixu(date))
    signer = PKCS1_v1_5.new(key)
    sign_auter = signer.sign(h)
    return sign_auter

# 私钥文件
priKey = '''-----BEGIN RSA PRIVATE KEY-----
MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAMtrfcrKrG41tG5aWNKJusCs9yVkdt4G5/Vg7QaRsSZiWOxsd/zs/aNuS9SuzL/YMrqYCRoil12nhqhxQDoQdncUIRwrc+HhjtshE9btMVJFWyFkUbaBA0DsPwMzGsVxhOByBKimoDjCL2I92fawv0IAJDhpd46kly0TGLf8DcbNAgMBAAECgYB+cX2KrXqLMwTJx40IqaYVGC6z5oPgtQhARZRwDeXAx0chBrd611E94lRuio0o/tlhlRmrTi8qfvS8BVF4Bj2r39Le3/wdzcVDoK8ruVRUW+S9JI+9p3WNVwIvderROg7ttcl67XV5jRYQqOsqDZa9f224luN0B4q41yzz2c2KAQJBAP5A2uQrmnY9mOkeCU6mveQpneP6c8w0rXIXFEyFKD3t/MjREb17/GRhSu/ZSXnzKW5F8C+d5dqXAFETBfH7k4ECQQDM0TzUg4i+i4xsQ9NPRZzBT1HI998DI2umjPfEYLGdCZvsEhV4B4rCKpVsNKdNWkNgdd6sKOj53n0yTBwjIulNAkEAilYrQv5eenslWaFYGw0qQJxMJiC9JJx8ypi4GLJSpO96HKF0b46oUs2FAl9NVSbyoec3uhDFYVvLdlFNaM4jAQJAULo71qtNb4UDQPzuwbT3Vv4ThzmjjdIdMRUo5x8RgoryCPcLvTaDy4oLQQ3zzzo/ijqLHKI3SZ0XDYcQJA0zlQJBAJvVdpJy8472UZvHXrrjG7//ohyiTNbYKLRU7mDtH1e2uQz+BI+lha4LlZaN3jFUssV1FnG0C7otaOKsF7s302Y=
-----END RSA PRIVATE KEY-----'''

# 公钥文件
pubKey = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDKoeRzRVf8WoRSDYYqUzThpYCr
90jfdFwTSXHJ526K8C6TEwdTUA+CFPQPRUg9jrYgFcown+J2myzO8BRLynD+XHb9
ilLb49Mqk2CvDt/yK32lgHv3QVx14Dpb6h8isjncSF965fxBxlHGbvPwnHkJ9etR
IYdYV3QpYohFszH3wQIDAQAB
-----END PUBLIC KEY-----'''
sign_data = {'name': "leslie", 'paassword': "a123456"}
sign = sign(sign_data,priKey)
print (b2a_hex(sign))


import base64
import rsa

def sign_new(prikey,data):
    pri_key = rsa.PrivateKey.load_pkcs1(prikey)
    signature = rsa.sign(str(paixu(data)), priv_key=pri_key, hash='SHA-1')
    return base64.b64encode(signature)

data = {"name":"leslie",
        "password":"a123456"}
a = sign_new(priKey,data)
print (a)