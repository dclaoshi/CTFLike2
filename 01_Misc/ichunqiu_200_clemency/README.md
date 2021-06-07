# clemency

## 题目描述
---
```

```

## 题目来源
---
第三届上海市大学生网络安全大赛

## 主要知识点
---
解密

## 题目分值
---
200

## 部署方式
---


## 解题思路
---
通过阅读文档发现clemency是middle edian，9bits perbyte，而且flag是存放在flag page里面，firmware的功能是将flag page输出，所以需要将输出的内容从9bits模式解码到8bits模式即可得到flag。

```python
f=open("./flag.enc","r")
flag_enc=f.read()
f.close()
flag=""
flag_enc_bin=""
c=0
for i in range(len(flag_enc)):
    flag_enc_bin+=bin(ord(flag_enc[i]))[2:].rjust(8,"0")
len_enc_bin=len(flag_enc_bin)
#print flag_enc_bin
for i in range(len_enc_bin/9):
    flag+=chr(int(flag_enc_bin[i*9:i*9+9],2))
print flag
```

## 参考
---
