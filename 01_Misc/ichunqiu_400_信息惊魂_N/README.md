# 信息惊魂

## 题目描述
---
```
通过dump出的手机数据，你能发现什么密码吗？

文件：点击下载附件

flag格式：flag{}
```

## 题目来源
---
JCTF 2014

## 主要知识点
---


## 题目分值
---


## 部署方式
---


## 解题思路
---

从data中可以找到curl请求⽹盘地址,由此下载pcap。

根据http://blog.flanker017.me/actf-misc300%E5%AE%98%E6%96%B9writeup/类似思路找到adb流量中的图片,得到 flag。

## 参考
---
