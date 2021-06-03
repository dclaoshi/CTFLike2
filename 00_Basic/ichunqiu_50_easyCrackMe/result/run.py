#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2021年5月31日17:07:20
@description : exe 解密
@Update date :   
"""  

import ctypes 

sox = [-85, -35, 51, 84, 53, -17]
hah = [0xfb, 0x9e,0x67, 0x12, 0x4e, 0x9d, 0x98, 0xAB, 0x0, 0x6, 0x46, 0x8A, 0x0F4, 0x0B4, 0x6, 0x0B, 0x43, 0xDC, 0xD9, 0x0A4, 0x6C, 0x31, 0x74, 0x9C, 0xD2, 0xA0,]

result = []
for i in range(0,26):
    # print sox[i%6], ctypes.c_ubyte(sox[i%6]).value
    print chr(hah[i] ^ ctypes.c_ubyte(sox[i%6]).value)
    result.append(chr(hah[i] ^ ctypes.c_ubyte(sox[i%6]).value))

print "".join(result)

