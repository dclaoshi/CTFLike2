# Bubble

## 题目描述
---
```
附件
```

## 题目来源
---
2017第二届广东省强网杯线上赛

## 主要知识点
---
Bubble Babble Encoding加密

## 题目分值
---
50

## 部署方式
---


## 解题思路
---

题目给出了 Bubble Babble Encoding 的密文，解密即可。

```python
# pip install bubblepy
from bubblepy import BubbleBabble

bb = BubbleBabble()
print bb.decode('xinik-samak-luvag-hutaf-fysil-notok-mepek-vanyh-zipef-hilok-detok-damif-cusol-fezyx')
```

flag{Ev3ry7hing_i5_bubb13s}

## 参考
---
