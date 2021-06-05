# 吃货

## 题目描述
---
```
麻辣烫的标配

flag{abbab_babbb_baaaa_aaabb}
```

## 题目来源
---
“百度杯”CTF比赛 十二月场

## 主要知识点
---
培根密码

## 题目分值
---
10

## 部署方式
---


## 解题思路
---
abbab_babbb_baaaa_aaabb
N_X_Q_D
flag{N_X_Q_D}
 
共有两种解码方法，其第一种解码规则如下：
A aaaaa B aaaab C aaaba D aaabb
E aabaa F aabab G aabba H aabbb
I abaaa J abaab K ababa L ababb
M abbaa N abbab O abbba P abbbb
Q baaaa R baaab S baaba T baabb
U babaa V babab W babba X babbb
Y bbaaa Z bbaab

第二种解码方法如下：
a AAAAA g AABBA n ABBAA t BAABA
b AAAAB h AABBB o ABBAB u-v BAABB
c AAABA i-j ABAAA p ABBBA w BABAA
d AAABB k ABAAB q ABBBB x BABAB
e AABAA l ABABA r BAAAA y BABBA
f AABAB m ABABB s BAAAB z BABBB

## 参考
---
