#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Cipher import ARC4
import binascii
import ctypes

def RC4_enc(data, key):
    rc41 = ARC4.new(key)
    encrypted = rc41.encrypt(data)
    return encrypted.encode('hex').upper()
 
def RC4_dec(data, key):
    rc41 = ARC4.new(key)
    encrypted = rc41.decrypt(data)
    return encrypted.encode('hex').upper()   

def RC4_dec_to_str(data, key):
    rc41 = ARC4.new(key)
    encrypted = rc41.decrypt(data)
    return encrypted

'''
 v7 = -99;
    v8 = -121;
    v9 = 113;
    v10 = -92;
    v11 = -125;
    v12 = 11;
    v13 = -86;
    v14 = 83;
    v15 = -60;
    v16 = 56;
    v17 = 54;
    v18 = -123;
'''

miwen = "UUyFTj8PCzF6geFn6xgBOYSvVTrbpNU4OF9db9wMcPD1yDbaJw==".decode("base64")
mingwen  = RC4_dec(miwen, "welcometoicqedu")
print mingwen
#print binascii.unhexlify(mingwen)



