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