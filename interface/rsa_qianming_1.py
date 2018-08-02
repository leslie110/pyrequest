#coding:utf-8

import cgi, base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from binascii import b2a_hex,a2b_hex


#私钥文件
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

#公钥文件
pubKey = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDKoeRzRVf8WoRSDYYqUzThpYCr
90jfdFwTSXHJ526K8C6TEwdTUA+CFPQPRUg9jrYgFcown+J2myzO8BRLynD+XHb9
ilLb49Mqk2CvDt/yK32lgHv3QVx14Dpb6h8isjncSF965fxBxlHGbvPwnHkJ9etR
IYdYV3QpYohFszH3wQIDAQAB
-----END PUBLIC KEY-----'''

'''*RSA签名
* data待签名数据
* 签名用商户私钥，必须是没有经过pkcs8转换的私钥
* 最后的签名，需要用base64编码
* return Sign签名
'''
def sign(data):
    key = RSA.importKey(priKey)
    h = SHA.new(data.encode())
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(h)
    return b2a_hex(signature)

'''*RSA验签
* data待签名数据
* signature需要验签的签名
* 验签用支付宝公钥
* return 验签是否通过 bool值
'''
def verify(data, signature):
    key = RSA.importKey(pubKey)
    h = SHA.new(data.encode())
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(h, a2b_hex(signature)):
        return True
    return False

raw_data = 'partner="2088701924089318"&seller="774653@qq.com"&out_trade_no="123000"&subject="123456"&body="2010新款NIKE 耐克902第三代板鞋 耐克男女鞋 386201 白红"&total_fee="0.01"¬ify_url="http://notify.java.jpxx.org/index.jsp"'
sign_data = sign(raw_data)
print (sign_data)
print (verify(raw_data, sign_data))
