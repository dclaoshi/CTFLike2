# 简单流量分析

## 题目描述
---
> 不久前，运维人员在日常安全检查的时候发现现场某设备会不时向某不知名ip发出非正常的ICMP PING包。这引起了运维人员的注意，他在过滤出ICMP包分析并马上开始做应急处理很可能已被攻击的设备。运维人员到底发现了什么?flag形式为 flag{}

## 题目来源
---
纵横网络靶场社区 https://game.fengtaisec.com/

## 主要知识点
---


## 附件
---


## 题目分值
---
20

## 部署方式
---


## 解题思路
---
ICMP包长度转为 ascii 码, 最后 base64 解码得  flag

```Python
#!/usr/bin/env python
# coding:utf-8
import base64
from scapy.all import rdpcap

packets=rdpcap("./fetus_pcap.pcap")
res = ""
for p in packets:
    if p.payload.payload.type == 8:
        l = len(p.payload.payload.payload)
        print(p.payload.payload.payload)
        print(l)
        res += chr(l)

print(res)
print(base64.b64decode(res))
```

![](images/ctf-2021-09-01-22-05-43.png)

## Flag
---
flag{xx2b8a_6mm64c_fsociety}

## 参考
---
