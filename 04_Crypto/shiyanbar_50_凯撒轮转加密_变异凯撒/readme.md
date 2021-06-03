## 变异凯撒

```
加密密文：afZ_r9VYfScOeO_UL^RWUc
格式：flag{ }
```

解题过程分这几部分，首先`afZ_r9VYfScOeO_UL^RWUc`的ascii码为
```
97 102 90 95 114 57 86 89 102 83 99 79 101 79 95 85 76 94 82 87 85 99
```
`flag{    }`的前几位ascii码为
```
102 108 97 103 123
```
按位做一个比较就可以发现102-97=5，108-102=6，97-90=7，所以此题目凯撒的规律为第一个字符ascii加5，其他每个字符按位ascii自增1，所以解密代码如下。解密代码如下
```python
#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-07
@description : 凯撒轮转密码解密
@Update date :   
"""  

INIT_ADD = 5

input = raw_input()
output = ""
for char in input:
    output += chr(ord(char) + INIT_ADD)
    INIT_ADD += 1
print output
```
输出
```
afZ_r9VYfScOeO_UL^RWUc
flag{Caesar_variation}
```
结束。