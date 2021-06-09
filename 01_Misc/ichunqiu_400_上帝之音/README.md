# 上帝之音

## 题目描述
---
```
这是一段神奇的声音，上帝之音似乎和无字天书一样，让我们这些凡人无法理解，琢磨不透，你能以上帝的角度，理解这段WAV的含义么？

文件：点击下载附件
```

## 题目来源
---
ISC2016训练赛——phrackCTF

## 主要知识点
---


## 题目分值
---
400

## 部署方式
---


## 解题思路
---

每个myisam表都有三个文件：.frm(储存表结构) .myd（储存数据） .myi（储存索引）
在 MySQL 5.7,默认引擎是innodb，如果要使用myisam，需要指定 engine=myisam。

```
$ dd if=godwave.wav of=test ibs=1 skip=611848 count=127806 
127806+0 records in
249+1 records out
127806 bytes (128 kB, 125 KiB) copied, 0.129562 s, 986 kB/s
```

## 参考
---
