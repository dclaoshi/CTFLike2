#-*- coding: UTF-8 -*- 
from base64 import *


hecheng = []

first = open("next/first", "rb")
first_content = first.read()
second = open("next/second", "rb")
second_contnet = second.read()

# 获取16进制数据
s1 = ''.join(map(b16encode,list(first_content)))
s2 = ''.join(map(b16encode,list(second_contnet)))
str=""
for i in range(0,len(s1)):
    str += s1[i] + s2[i];
str = str.decode('hex')
with open(r'flag.jpg','wb') as f:
    f.write(str)