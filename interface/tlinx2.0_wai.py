# encoding=utf-8
from Crypto.Cipher import AES
from Crypto.Hash import MD5,SHA
import json,time,requests
from binascii import b2a_hex,a2b_hex


def paixu(sha_data):
    sha_data = sorted(sha_data.items())
    param = []
    for _key, _value in sha_data:
        param.append(_key + "=" + _value)
    # print (('&'.join(param).encode()))
    return ('&'.join(param).encode())

# 使用sha1加密然后md5加密成签名
def sign(data):
    sha1 = SHA.new(paixu(data))
    # print (sha1.hexdigest())
    sign = MD5.new(bytes(sha1.hexdigest(),'utf-8'))
    return sign.hexdigest()

def request(url,data):
    r = requests.post(url,data=data)
    result = r.json()
    return result

def aes_data(text):
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    text = json.dumps(text, separators=(',', ':'))
    # print(pad(text))
    key = b'332ab03d200c1918fb6d7beb2266efb6'
    aes = AES.new(key, AES.MODE_ECB)
    encrypted_text = b2a_hex(aes.encrypt(bytes(pad(text), 'utf-8')))
    return str(encrypted_text, 'utf-8')

def aes_jiemi(data):
    # 秘钥
    key = b'332ab03d200c1918fb6d7beb2266efb6'
    # 密文
    text = data
    # 初始化加密器
    aes = AES.new(key, AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    #
    # decrypted_text = a2b_hex(aes.decrypt(text)) # 执行解密密并转码返回str
    decrypted_text = aes.decrypt(a2b_hex(text))
    return str(decrypted_text,'unicode-escape')



timestamp = int(time.time())
sign_data = {"timestamp":str(timestamp),
             "open_id":"cbca47b3b0f0c7e94bd1c9c6fb94dbb7",
             "open_key":"332ab03d200c1918fb6d7beb2266efb6",
             "pmt_type":"0,1,2,3"
             }
data = {"open_id": "cbca47b3b0f0c7e94bd1c9c6fb94dbb7",
        "timestamp":str(timestamp),
        "sign":sign(sign_data),
        "pmt_type":"0,1,2,3"
        }
url = "https://api.tlinx.com/mct1/paylist"
message = request(url,data)
print (message)
print (aes_jiemi((message['data'])))
a = aes_jiemi(message['data'])
print (type(a))
