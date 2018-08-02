# coding=utf-8
#AES-demo

import base64,json
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from collections import OrderedDict

'''
采用AES对称加密算法
'''
# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes
#加密方法
def encrypt_oracle():
    # 秘钥
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    key = b'2e8a490fd9745a68d1930aabcacb3a6a'
    # 待加密文本
    data = OrderedDict([("paymentCode","1000000477581663"),
                           ("merchantId","20160000"),
                           ("list","[{\"cashierId\":\"213639\",\"payAmt\":10,\"scode\":\"1000000458046259\"}]")
                           ])
    text = json.dumps(data,separators=(',',':'))
    # 初始化加密器
    aes = AES.new(key, AES.MODE_ECB)
    print (text)
    print (pad(text))

    #先进行aes加密
    encrypted_text = b2a_hex(aes.encrypt(bytes(pad(text))))
    print(encrypted_text)

#解密方法
def decrypt_oralce():
    # 秘钥
    key = b'2e8a490fd9745a68d1930aabcacb3a6a'
    # 密文
    text = 'cdbcd3c3b88d69f9354ec981d39918a7b4d1124d1948255f32410c3681485afb0a6216899e887fcf6290f095b32a2f366666bd75456ce6e21fb01f7b95c78d2f26db3e29a719268cd6fbaf20929532ee4ed7b73b0be867040a5717ec6811599a74e5171c7dd667ee5f3ea18773280ae500354971f9ff4c6dce4e0a04b86f115fb25a81ac206f42717b9e1467b1191c35'
    # 初始化加密器
    aes = AES.new(key, AES.MODE_ECB)
    #优先逆向解密base64成bytes
    #
    # decrypted_text = a2b_hex(aes.decrypt(text)) # 执行解密密并转码返回str
    decrypted_text = aes.decrypt(a2b_hex(text))
    print(decrypted_text)

if __name__ == '__main__':

    encrypt_oracle()
    decrypt_oralce()