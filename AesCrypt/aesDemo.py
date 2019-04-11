#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者：liux
日期：2018/11/14 14:17
功能：使用pycrypto模块实现AES加密解密
"""
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)      #\0 中\为转义
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        str='\0'.encode('utf-8')   #把‘\0’转为utf-8 的bytes形式
        return plain_text.rstrip(str)


if __name__ == '__main__':
    # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
    secret_key='A0Zr98jX?>HHLiuX'
    pc = prpcrypt(secret_key)
    e = pc.encrypt("123@56?")
    d = pc.decrypt(e)

    print(e)
    print(d.decode('utf-8'))





