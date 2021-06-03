# 手贱的A君

## 题目描述
---
某天A君的网站被日，管理员密码被改，死活登不上，去数据库一看，啥，这密码md5不是和原来一样吗？为啥登不上咧？

d78b6f302l25cdc811adfe8d4e7c9fd34

请提交PCTF{原来的管理员密码}

## 题目来源
---
ichunqiu ISC2016训练赛——phrackCTF

## 主要知识点
---
md5解密

## 题目分值
---
50

## 部署方式
---
无

## 解题思路
---
发现题目给出的md5是33位，所以遍历删除一个字符，进行md5批量解密。

```python
>>> a = "d78b6f302l25cdc811adfe8d4e7c9fd34"
>>> def ff(str,num):
...     return str[:num] + str[num+1:];
... 
>>> for i in range(0,33):
...     print ff(a,i)

78b6f302l25cdc811adfe8d4e7c9fd34
d8b6f302l25cdc811adfe8d4e7c9fd34
d7b6f302l25cdc811adfe8d4e7c9fd34
d786f302l25cdc811adfe8d4e7c9fd34
d78bf302l25cdc811adfe8d4e7c9fd34
d78b6302l25cdc811adfe8d4e7c9fd34
d78b6f02l25cdc811adfe8d4e7c9fd34
d78b6f32l25cdc811adfe8d4e7c9fd34
d78b6f30l25cdc811adfe8d4e7c9fd34
d78b6f30225cdc811adfe8d4e7c9fd34
d78b6f302l5cdc811adfe8d4e7c9fd34
d78b6f302l2cdc811adfe8d4e7c9fd34
d78b6f302l25dc811adfe8d4e7c9fd34
d78b6f302l25cc811adfe8d4e7c9fd34
d78b6f302l25cd811adfe8d4e7c9fd34
d78b6f302l25cdc11adfe8d4e7c9fd34
d78b6f302l25cdc81adfe8d4e7c9fd34
d78b6f302l25cdc81adfe8d4e7c9fd34
d78b6f302l25cdc811dfe8d4e7c9fd34
d78b6f302l25cdc811afe8d4e7c9fd34
d78b6f302l25cdc811ade8d4e7c9fd34
d78b6f302l25cdc811adf8d4e7c9fd34
d78b6f302l25cdc811adfed4e7c9fd34
d78b6f302l25cdc811adfe84e7c9fd34
d78b6f302l25cdc811adfe8de7c9fd34
d78b6f302l25cdc811adfe8d47c9fd34
d78b6f302l25cdc811adfe8d4ec9fd34
d78b6f302l25cdc811adfe8d4e79fd34
d78b6f302l25cdc811adfe8d4e7cfd34
d78b6f302l25cdc811adfe8d4e7c9d34
d78b6f302l25cdc811adfe8d4e7c9f34
d78b6f302l25cdc811adfe8d4e7c9fd4
d78b6f302l25cdc811adfe8d4e7c9fd3
```

在站点[https://www.somd5.com/batch.html](https://www.somd5.com/batch.html)批量进md5解密。

![](images/2020-05-09-11-05-05.png)

可以看到密码位hack

PCTF{hack}
