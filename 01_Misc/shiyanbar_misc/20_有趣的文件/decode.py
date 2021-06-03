#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Create date : 2021年6月1日21:13:43
@description : 将HEX转储文件转为原始bin文件
@Update 
"""

import binascii

f = open('funfile.txt', 'r')
text = f.read()
text = text.split()

for i in text:
    if len(i) == 7:
        text.remove(i)

text.insert(0, '7a37')

with open('funfile_output.zip', 'wb') as g:
    output = b''
    for i in text:
        tmpa = i[:2]
        tmpb = i[2:]
        new_byte = tmpb + tmpa
        output += binascii.a2b_hex(new_byte)
    g.write(output)