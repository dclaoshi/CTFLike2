#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-11
@description : WTF
@Update date :   
"""  

import sys
from PIL import Image

file = open("code.txt","r")
content = file.read().decode("base64")
length = len(content)

size = (256,256)
image = Image.new("RGB", size, (255,255,255))
data = image.getdata()
xy = (0, 0)
for i in range(length):
    try:
        if content[i] == '1':
            xy = (i/256,i%256)
            data.putpixel(xy,(0, 0, 0))
    except :
        pass
image.save("result.png")