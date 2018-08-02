# coding=utf-8
import base64,hashlib,json
from Crypto.Cipher import AES
import requests
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


def paixu(sha_data):
    # 将字典进行排序并转成&字符串格式
    sha_data = sorted(sha_data.items())
    param = []
    for _key, _value in sha_data:
        param.append(_key + "=" + _value)
    return ('&'.join(param).encode())

def sign(date, prikey):
    # sha_data = sorted(date.items())
    # param = []
    # for _key, _value in sha_data:
    #     param.append(_key + "=" + _value)
    # print('&'.join(param))
    key = RSA.import_key(prikey)
    h = SHA.new(paixu(date))
    signer = PKCS1_v1_5.new(key)
    sign_auter = signer.sign(h)
    sign = base64.urlsafe_b64encode(sign_auter)[0:-1]
    # sha1 = hashlib.sha1()
    # sha1.update(paixu(date))
    # print(sha1.hexdigest())
    return sign

def aes(date):
    obj = AES.new(b'this is a key123', AES.MODE_CBC, b'this is an IV456')
    pad = lambda s :s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    message = pad(json.dumps(date))
    date = obj.encrypt(message.encode())
    return base64.b64encode(date)

def login(url,data):
    r = requests.post(url,data=data)
    result = r.json()
    return result

# 私钥文件
priKey = '''-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDKoeRzRVf8WoRSDYYqUzThpYCr90jfdFwTSXHJ526K8C6TEwdT
UA+CFPQPRUg9jrYgFcown+J2myzO8BRLynD+XHb9ilLb49Mqk2CvDt/yK32lgHv3
QVx14Dpb6h8isjncSF965fxBxlHGbvPwnHkJ9etRIYdYV3QpYohFszH3wQIDAQAB
AoGAFhKqkw/ztK6biWClw8iKkyX3LURjsMu5F/TBK3BFb2cYe7bv7lhjSBVGPL+c
TfBU0IvvGXrhLXBb4jLu0w67Xhggwwfc86vlZ8eLcrmYVat7N6amiBmYsw20GViU
UFmePbo1G2BXqMA43JxqbIQwOLZ03zdw6GHj6EVlx369IAECQQD4K2R3K8ah50Yz
LhF7zbYPIPGbHw+crP13THiYIYkHKJWsQDr8SXoNQ96TQsInTXUAmF2gzs/AwdQg
gjIJ/dmBAkEA0QarqdWXZYbse1XIrQgBYTdVH9fNyLs1e1sBmNxlo4QMm/Le5a5L
XenorEjnpjw5YpEJFDS4ijUI3dSzylC+QQJARqcD6TGbUUioobWB4L9GD7SPVFxZ
c3+EgcxRoO4bNuCFDA8VO/InP1ONMFuXLt1MbCj0ru1yFCyamc63NEUDAQJBALt7
PjGgsKCRuj6NnOcGDSbDWIitKZhnwfqYkAApfsiBQkYGO0LLaDIeAWG2KoCB9/6e
lAQZnYPpOcCubWyDq4ECQQCrRDf0gVjPtipnPPS/sGN8m1Ds4znDDChhRlw74MI5
FydvHFumChPe1Dj2I/BWeG1gA4ymXV1tE9phskV3XZfq
-----END RSA PRIVATE KEY-----'''

# 公钥文件
pubKey = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDKoeRzRVf8WoRSDYYqUzThpYCr
90jfdFwTSXHJ526K8C6TEwdTUA+CFPQPRUg9jrYgFcown+J2myzO8BRLynD+XHb9
ilLb49Mqk2CvDt/yK32lgHv3QVx14Dpb6h8isjncSF965fxBxlHGbvPwnHkJ9etR
IYdYV3QpYohFszH3wQIDAQAB
-----END PUBLIC KEY-----'''
base_url = ''
sign_data = {'name': "leslie", 'paassword': "a123456"}
sign = sign(sign_data, priKey).decode()
print(sign)
aes_date = aes(sign_data)
print (aes_date)
data = {'sign':sign,'data':aes_date}
# status = login(base_url,data)
