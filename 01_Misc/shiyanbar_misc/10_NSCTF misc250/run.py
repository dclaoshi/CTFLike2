#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-11
@description : 生成密码表
@Update date :   
"""  

f = open("dict.txt","w")
for i in range(1,100000):
    f.write("nsfocus%05d\n"%i)
f.close()