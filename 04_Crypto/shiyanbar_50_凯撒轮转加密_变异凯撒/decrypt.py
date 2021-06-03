#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-07
@description : 凯撒轮转密码解密
@Update date :   
"""  

INIT_ADD = 5

input = raw_input()
output = ""
for char in input:
    output += chr(ord(char) + INIT_ADD)
    INIT_ADD += 1
print output