#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2021年5月31日17:07:20
@description : USB流量解码
@Update date :   
"""  

hids_codes = {"0x04":"a","0x05":"b","0x06":"c","0x07":"d","0x08":"e","0x09":"f","0x0A":"g","0x0B":"h","0x0C":"i","0x0D":"j","0x0E":"k","0x0F":"l","0x10":"m","0x11":"n","0x12":"o","0x13":"p","0x14":"q","0x15":"r","0x16":"s","0x17":"t","0x18":"u","0x19":"v","0x1A":"w","0x1B":"x","0x1C":"y","0x1D":"z","0x1E":"1","0x1F":"2","0x20":"3","0x21":"4","0x22":"5","0x23":"6","0x24":"7","0x25":"8","0x26":"9","0x27":"0","0x36":",","0x33":":","0x28":"\n","0x2C":" ","0x2D":"_","0x2E":"=","0x2F":"{","0x30":"}"}
layout_dvorak = { 'q':"'", 'w':',', 'e':'.', 'r':'p', 't':'y', 'y':'f', 'u':'g', 'i':'c', 'o':'r', 'p':'l', '_':'_', ':':'S','[':'/', '{':'{', '}':'}' ,']':'=','a':'a', 's':'o', 'd':'e', 'f':'u', 'g':'i', 'h':'d', 'j':'h', 'k':'t', 'l':'n', ';':'s', "'":'-','z':';', 'x':'q', 'c':'j', 'v':'k', 'b':'x', 'n':'b', 'm':'m', ',':'w', '.':'v', '.':'z',' ':' ','Q':"'", 'W':',', 'E':'.', 'R':'P', 'T':'Y', 'Y':'F', 'U':'G', 'I':'C', 'O':'R', 'P':'L','A':'A', 'S':'O', 'D':'E', 'F':'U', 'G':'I', 'H':'D', 'J':'H', 'K':'T', 'L':'N', ';':'S', "'":'-','Z':';', 'X':'Q', 'C':'J', 'V':'K', 'B':'X', 'N':'B', 'M':'M','0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','7':'7','8':'8','9':'9'}
flag = ''
file = open('usbdata.txt','r') 
for line in file.readlines():
    spli = line.split(':')
    conv = '0x'+spli[2].upper()
    if conv in hids_codes:
        if spli[0] == '00':
            flag += layout_dvorak[hids_codes[conv]]
        else:
            flag += layout_dvorak[hids_codes[conv].upper()]

print(flag)