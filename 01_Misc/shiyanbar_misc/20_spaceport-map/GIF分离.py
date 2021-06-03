#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import os

gilFileName = 'spaceportmap.gif'        # 将准备好的gif 打开
im = Image.open(gilFileName)
pngDir = gilFileName[:-4]        # 获取 .gif 前面的字符，也就是名字

if not os.path.exists(pngDir):
    '''如果没有重名的文件夹，就生成这个文件夹来存放图片'''
    os.mkdir(pngDir)         

try:      
    '''while True 的作用就是不停的遍历gif，取得每一个图片，如果图片访问结束 会报错，所以 try一下'''
    while True:     
        current = im.tell()       # 获取img对象的 帧图片
        im.save(pngDir + '/' + str(current) + '.png')      # 保存
        im.seek(current + 1)     # seek的作用就相当于 装饰器的 next，代表下一个
            # current 代表帧图片，+1 就是下一张

except EOFError:
    pass
