# 传感器2

## 题目描述
---
```
现有某ID为0xFED31F的压力传感器，已知测得压力为45psi时的未解码报文为：
5555555595555A65556A5A96AA666666A955
压力为30psi时的未解码报文为：
5555555595555A65556A9AA6AA6666665665
请给出ID为0xFEB757的传感器在压力为25psi时的解码后报文，提交hex。

注：其他测量读数与上一个传感器一致。
tips：flag是flag{破译出的明文}
```

## 题目来源
---
2016全国大学生信息安全竞赛

## 主要知识点
---


## 题目分值
---
300

## 部署方式
---


## 解题思路
--- 

先对两个内容进行解码，解码代码如下

```
0xFED31F 45psi  5555555595555A65556A5A96AA666666A955
0xFED31F 30psi  5555555595555A65556A9AA6AA6666665665
```

```python
#!/user/bin/env python2
# -*-coding:utf-8 -*-

n = 0x5555555595555A65556A5A96AA666666A955
flag = ''
bs = '0'+bin(n)[2:]
r = ''

def conv(s):
    return hex(int(s, 2))[2:]

for i in range(0, len(bs), 2):
    if bs[i:i+2] == '01':
        r += '1'
    else:
        r += '0'
        
for i in range(0, len(r), 8):
    tmp = r[i:i+8][::-1]
    flag += conv(tmp[:4])
    flag += conv(tmp[4:])

print flag.upper()
```

解码结果 
```
0xFED31F 45psi  FFFFFED31F635055F8
0xFED31F 30psi  FFFFFED31F425055D7
```

对比两串字符发现两处地方不同，且都相差33，分别为（63、42）（F8、D7）

由25和30差5，30和45差15，则新值应该是 (0x42-(0x63-0x42)/15*5)，为 `FFFF FEB757 37 5055 xx`

最后一个字节作为校验位和校验算法是CRC

hex(bin(0xfe+0xb7+0x57+0x37+0x50+0x55)) = 0b1011101000 = 0xe8

所以最终的结果为 FFFF FEB757 37 5055 E8

flag{FFFFFEB757375055E8}

## 参考
---
