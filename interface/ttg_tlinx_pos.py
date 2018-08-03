# coding=utf-8
from Crypto.Cipher import AES,PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from binascii import b2a_hex,a2b_hex
from collections import OrderedDict
import json,base64
import requests

# sha1加密
def sha_pwd(data):
    sha1 = SHA.new(data.encode())
    return sha1.hexdigest()

# 公钥rsa加密
def pub_rsa_pwd(pub_key,data):
    rsakey = RSA.importKey(pub_key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = b2a_hex(cipher.encrypt(bytes(json.dumps(data),'utf-8')))
    return str(cipher_text,'utf-8')

def first_login(url,data):
    r = requests.post(url,data=data)
    result = r.json()
    return result

# 解密
def jiemi(key,cipher_text):
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(a2b_hex(cipher_text))
    return text



pub_key ='''MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu7MeQFgB+ICkWcCOcsCXduRTKCQO8vc7yD0cmVvxNLY+LNomJYRX4TL6SCPYvRbsgpiwGaxaJgcZ3mYrBerbSV5dxqqas5FKL85+Smxu+70f9QkOk/NiWa35Yc/EdqalbRAajmjju11wV5FDtjC90+vWQvO393VkLK52awdtA9fScx0wnW5DbYTWN4nTAFg2Jc8ZGcM76t3bgt/OCBj95/D9GbU9QFSk4eIanwlzWZpb7jeJdzss3LPAZBdFQVggBLDnmjK+1S0YFAPd1FME+PJWLXQS1Wbf2jaZV7tg2OWReZR3aqqTWpaUEEowg0JQQGjMUs8bGj5bXn1jJ95V7QIDAQAB'''
prv_key = '''-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7sx5AWAH4gKRZ
wI5ywJd25FMoJA7y9zvIPRyZW/E0tj4s2iYlhFfhMvpII9i9FuyCmLAZrFomBxne
ZisF6ttJXl3GqpqzkUovzn5KbG77vR/1CQ6T82JZrflhz8R2pqVtEBqOaOO7XXBX
kUO2ML3T69ZC87f3dWQsrnZrB20D19JzHTCdbkNthNY3idMAWDYlzxkZwzvq3duC
384IGP3n8P0ZtT1AVKTh4hqfCXNZmlvuN4l3Oyzcs8BkF0VBWCAEsOeaMr7VLRgU
A93UUwT48lYtdBLVZt/aNplXu2DY5ZF5lHdqqpNalpQQSjCDQlBAaMxSzxsaPlte
fWMn3lXtAgMBAAECggEBAJs9Ioj/AOpBoyxkGKyJ4vu/DZPGduK2XihXet7P7ye0
jqnT5vbihThJTDz8ANcrLYM5u3QQWyLWfqu0/mJPgvwkYxTbp0VapevyMftlwUjN
e6/SxM7S3gXj4Lzn9MpZO7p/NieQUsF1H2QdTc5Sc73hcP1Ay2eMHMTjqicNJjml
C46d2RZr/O3ZZK0PeR+ub7TIzfFfm5K5Qb3wPkVuNAZWdrf5W4VTYEvwDgU3qtRr
RPcWDWSGb0ahoX5c6sc2A6DlZDXzJVOWhI171+URXaJWZlITErfLFvWGosbfqf/r
iHi5xNdYYKjliyZa8mKTqtV6uKPbFkuwYvFSKN1QgiECgYEA7qJcLO4ucO3moF6H
yCQkcYv0CB4quODr7I1lEtTcelVRW+Aj/ecz6LB2nZpG6GuOcZ7K6XiMx09jILVO
gE4/Wa5coii+IdWQCsv91AAA2v1N/0cMeAdvsiJWz+saE9sWJ/lCKNyUNMWC+jVA
6HC9O3zzCFhsZuTHl23KKR3at9UCgYEAyVvfUFGGqSFx4yo6fGec19dmBv4qzBLT
N7hlqTiljQ8FHMCjwlxNXUmy91oiVFAXLYMOUGtUYdqFo4Dw5l5sQk579T//3BlN
czQP+BN67yja3Pu8kBCrT0lNMX9lqz7M+llqycNVUnY8CMVLv9SjmCk4Bq7Lo3ZS
S9YJ0mB1CbkCgYAO50r0b2etG96Ec4LtZ/xyrvftrdyjMUDqxCXk2DBw33U2VLhK
ui7OwH6X9zOoflcmF3G6xRGdvQKG32vorXpdYntckUjWmhzl37mZjOqAwsMlR02r
DWPXbzeWwqsdRFiM5I9SN/x1k0RL1hmYqrnWxkXzZnpWrsEcXvn6OWgYhQKBgB25
DAvFHQWWRENuFlgKy2IpD4x0tEiPdtJAy/Dgxb8+ulh2LzYffeQJXvuYOH0NnX5A
XDqOvVP8d8Gc5PJ8eaqH/1BCdDg/G+mng7vw1DK9ayE3n6v8ae04OsbVsWJH0OYb
kOHbjZqwjUgWJ4pXjxaE7xo9bx3f92HuZGDDkEMxAoGAAO12kUIe5HR+b2tIRYHX
WjIFFVTdAIXMU+rRLe0f5OWxPO+RAbcb/DzsUcOHximP0W/2R1Gh0/pjQYE4cVBw
3PZpdzFJOqlYMq8Scz68m5sheETDLpLwErnZbdcs1rw0cYtrdDBX/9Uy0oRjCSkF
G7o2dZQa/skesD9vO4rqcxw=
-----END PRIVATE KEY-----'''
password = sha_pwd("a123456")
data = OrderedDict([("name","leslie"),
                    ("password",password),
                    ("app","ios"),
                    ("device_code","7523C64626AC822A1C2C0358F49B6247")])
a = pub_rsa_pwd(base64.b64decode(pub_key),data)
print (a)
end = first_login("http://openapi.tlinx.cn/mct1/user/login",a)
print (end)
data_add = OrderedDict([("name","leslie"),
                    ("password",password),
                    ("app","ios"),
                    ("device_code","7523C64626AC822A1C2C0358F49B6247")])

data_add['openid'] = '1154545'
print (data_add)