# -*- coding:utf8 -*-
from Crypto.Cipher import AES

key = "copy__white__key"

obj = AES.new(key,AES.MODE_ECB)
c_file = open("gogogo/AES.encryt", "rb")
zip_data = obj.decrypt(c_file.read())

with open('next.zip','wb') as f:
    f.write(zip_data)