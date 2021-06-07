#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from random import randint
from math import floor, sqrt

def encrypt():
    miwen = ''
    mignwen = 'test'
    mingwen_ord_arr = [ ord(i) for i in mignwen ]
    random_int_vaule = randint(65, max(mingwen_ord_arr)) * 255
    for index in range(len(mignwen)):
        miwen += str(int(floor(float(random_int_vaule + mingwen_ord_arr[index]) / 2 + sqrt(random_int_vaule * mingwen_ord_arr[index])) % 255)) + ' '

    print miwen

def confirm_random_value():
    miwen = "208 140 149 236 189 77 193 104 202 184 97 236 148 202 244 199 77 122 113"
    miwen_ord_arr = miwen.split(" ")
    for n in xrange(65,127):  # n 为 random_value, 127的原因是明文的范围为可见字符，则最大为127，根据题目本身最小为65
        mingwen_right_count = 0
        for miwen_ord in miwen_ord_arr:  # 对每一个密文都要能够找到一个可见字符计算出来
            for x in xrange(33,128):  # 明文为可见字符，所以范围是33-128
                if int(floor(float(n*255 + x) / 2 + sqrt(n*255 * x)) % 255)==int(miwen_ord):  #
                    mingwen_right_count += 1
                    break
        if mingwen_right_count == len(miwen_ord_arr):  # 每个密文都能找到可见字符
            print n

def decrypt():
    miwen = "208 140 149 236 189 77 193 104 202 184 97 236 148 202 244 199 77 122 113"
    miwen_ord_arr = miwen.split(" ")
    random_value = 115
    mingwen_arr = []
    for miwen_ord in miwen_ord_arr:  # 对每一个密文都要能够找到一个可见字符计算出来
        for x in xrange(33,128):  # 明文为可见字符，所以范围是33-128
            if int(floor(float(random_value*255 + x) / 2 + sqrt(random_value*255 * x)) % 255)==int(miwen_ord):  #
                #print x, chr(x)
                if x > 65 and x < 127:
                    mingwen_arr.append(x)
        #print ""
    print "".join([chr(x) for x in mingwen_arr])
    

decrypt()

