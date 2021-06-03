#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-11
@description : Base64 to file
@Update date :   
@User : python run.py a.txt
"""  
import sys

input = sys.argv[1]
f = open(input,"rb")
content = f.read().decode("base64")
f.close()
f = open(input + "_decode","w")
f.write(content)
f.close()