# 听说是rc4算法

## 题目描述
---
```
key welcometoicqedu 

密文UUyFTj8PCzF6geFn6xgBOYSvVTrbpNU4OF9db9wMcPD1yDbaJw== 
```

## 题目来源
---
“百度杯”CTF比赛 十月场

## 主要知识点
---
rc4

## 题目分值
---
10

## 部署方式
---


## 解题思路
---

使用标准的rc4算法进行解密，发现无法解密成功。

思考无果后查询writeup，发现使用了这样的解法。

在算法中，将密文base64解码后的值的前16字节作为盐和题目给出的key，一起sha1后，作为解密算法的key。然后下面才是真正的rc4算法。

```python
import random, base64
import hashlib

def crypt(data, key) :
    s = [0] * 256
    for i in range(256) :
        s[i] = i
    # print(s)
    j = 0
    for i in range(256) :
        j = (j + s[i] + key[i % len(key)]) % 256
        # print(j)
        s[i], s[j] = s[j], s[i]
    i = 0
    j = 0
    res = ""
    for c in data :
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        res = res + chr(c ^ s[(s[i] + s[j]) % 256])
    return res

def tdecode(data, key) :
    data = base64.b64decode(data)
    salt = data[:16]
    return crypt(data[16:], hashlib.sha1(bytes(key,encoding = "utf8") + salt).digest())

if __name__ =='__main__':
    key = "welcometoicqedu"
    data = "UUyFTj8PCzF6geFn6xgBOYSvVTrbpNU4OF9db9wMcPD1yDbaJw=="
    print(tdecode(data,key))
```

## 参考
---
