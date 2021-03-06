# Matrix

## 题目描述
---
```
I like to approach problems with a fresh perspective and try to visualize the problem at hand. matrix.txt
```

## 题目来源
---
IceCTF

## 主要知识点
---


## 题目分值
---
90

## 部署方式
---


## 解题思路
---

将题目给出的16进制数字分解成2进制字符串，然后将2进制字符串转为二维码。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image
import numpy as np

def hex2bin(hexmat):
   binmattemp = [bin(m)[2:] for m in hexmat]
   rowlen = max([len(m) for m in binmattemp])
   binmat = [[0]+[int(b) for b in row.zfill(rowlen)] for row in binmattemp]

   print rowlen+1, 'x', len(binmat)
   for i in xrange(len(binmat)):
       print ''.join([str(b) for b in binmat[i]])

   return binmat, rowlen+1, len(binmat)

def rm_col(binmat, col):
   return [row[:col]+row[col+1:] for row in binmat]


def make_bw_img(binmat, w, h, outfilename, blackbit=0):

   bwmat = [[0 if b==blackbit else 255 for b in row] for row in binmat]

   imagesize = (w, h)
   img = Image.fromarray(np.uint8(np.array(bwmat)))
   img.save(outfilename)

if __name__ == '__main__':
   hexmat = [0x00000000,
             0xff71fefe,
             0x83480082,
             0xbb4140ba,
             0xbb6848ba,
             0xbb4a80ba,
             0x83213082,
             # 0xff5556fe,
             0xff5556fe,
             0x00582e00,
             0x576fb9be,
             0x707ef09e,
             0xe74b41d6,
             0xa82c0f16,
             0x27a15690,
             0x8c643628,
             0xbfcbf976,
             0x4cd959aa,
             0x2f43d73a,
             0x5462300a,
             0x57290106,
             0xb02ace5a,
             # 0xef53f7fc,
             0xef53f7fc,
             0x00402e36,
             0xff01b6a8,
             0x83657e3a,
             0xbb3b27fa,
             0xbb5eaeac,
             0xbb1017a0,
             0x8362672c,
             0xff02a650,
             0x00000000]

   binmat, w, h = hex2bin(hexmat)
   binmat = rm_col(binmat, 22)
   binmat = rm_col(binmat, 7)
   make_bw_img(binmat, w, h, 'matrix_rmcol.png', blackbit=1)
```

IceCTF{1F_y0U_l0oK_c1Os3lY_EV3rY7h1N9_i5_1s_4nD_0s}

## 参考
---
