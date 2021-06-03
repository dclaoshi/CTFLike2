# Base64

## 题目描述
---
GUYDIMZVGQ2DMN3CGRQTONJXGM3TINLGG42DGMZXGM3TINLGGY4DGNBXGYZTGNLGGY3DGNBWMU3WI===

## 题目来源
---
ichunqiu ISC2016训练赛——phrackCTF

## 主要知识点
---
base32

## 题目分值
---
50

## 部署方式
---
无

## 解题思路
---
题目名称是误导人的，使用base32解码即可。

```python
>>> a = "GUYDIMZVGQ2DMN3CGRQTONJXGM3TINLGG42DGMZXGM3TINLGGY4DGNBXGYZTGNLGGY3DGNBWMU3WI==="
>>> import base64
>>> base64.b32decode(a)
'504354467b4a7573745f743373745f683476335f66346e7d'
>>> base64.b32decode(a).decode("hex")
'PCTF{Just_t3st_h4v3_f4n}'
```
