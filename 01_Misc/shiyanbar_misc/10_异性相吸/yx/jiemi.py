#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2021年5月31日
@description : 异或解析
@Update date :   
"""  

with open("明文.txt") as f1:
    a = f1.read()
with open("密文.txt") as f2:
    b = f2.read()
 
key = ''
for i in range(len(a)):
    key += chr(ord(list(a)[i]) ^ ord(list(b)[i]))
print(key)