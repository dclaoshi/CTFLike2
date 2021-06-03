#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
合成图片
"""

import re
 
png_head = '\x89PNG\x0D\x0A\x1A\x0A\x00\x00\x00\x0DI'
 
# 获取数据包字节顺序信息
def get_index(flag=False):
    with open(filename, "rb") as f:
        data = f.read()
        rep = re.search(r'Content-Range: bytes (\d*)-(\d*)/(\d*)', data)
        if flag:
            return data, rep
        else:
            return rep
 
# 获取每个流的起始字节数
num = {}
for i in range(23):
    filename = str(i) + '.txt'
    idx = get_index()
    num[int(idx.group(1))] = i

newd = sorted(num.keys())

print num
print newd

# 按流起始字节数逐个将流写入png文件
with open("new.png", "wb") as f:
    # 写入文件头
    f.write(png_head)
    # flag标志当前文件末字节数
    flag = 12
    while newd:
        filename = str(num[newd[0]]) + '.txt'
        data, rep = get_index(True)
        idx = rep.regs[-1][1] + 2
        tmp = int(rep.group(2))
        print idx, tmp
        # 当前数据包已经被写入文件，不进行写操作
        if tmp < flag:
            newd.remove(newd[0])
            print '.'
            continue
        # 当前数据包被部分写入文件，从上个数据包末尾开始写操作
        elif newd[0] < flag:
            idx += flag - newd[0] + 1
        f.write(data[idx:])
        flag = tmp
        print idx, flag
        newd.remove(newd[0])