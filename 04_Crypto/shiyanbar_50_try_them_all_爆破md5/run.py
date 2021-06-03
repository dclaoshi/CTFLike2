#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-07
@description : md5爆破 单进程
@Update date :   
"""  


import string
import hashlib

endOutput = "5948"

file=open("output.txt","a")
md5input=raw_input("请输入md5：\n")
md5input=md5input.lower()

# apt=string.printable[:-6]
apt=string.letters

def dfs(s,num):
    m=hashlib.md5()
    print s + endOutput
    m.update(s + endOutput)
    md5temp=m.hexdigest()
    if md5temp==md5input:
        file.write("md5是："+md5input+"   明文是："+s+"\n")
        file.close()
        exit(-1)
    if len(s)==num:
        return
    for i in apt:
        dfs(s+i,num)
 
myinput=7               #生成字符的位数
for j in range(1,myinput):
    dfs("",j)
