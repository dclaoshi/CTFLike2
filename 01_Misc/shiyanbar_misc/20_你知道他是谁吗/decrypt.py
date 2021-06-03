#!/usr/bin/env python
#-*- coding: utf-8 -*-

#存储密码器
jwc=['ZWAXJGDLUBVIQHKYPNTCRMOSFE',
     'KPBELNACZDTRXMJQOYHGVSFUWI',
     'BDMAIZVRNSJUWFHTEQGYXPLOCK',
     'RPLNDVHGFCUKTEBSXQYIZMJWAO',
     'IHFRLABEUOTSGJVDKCPMNZQWXY',
     'AMKGHIWPNYCJBFZDRUSLOQXVET',
     'GWTHSPYBXIZULVKMRAFDCEONJQ',
     'NOZUTWDCVRJLXKISEFAPMYGHBQ',
     'QWATDSRFHENYVUBMCOIKZGJXPL',
     'WABMCXPLTDSRJQZGOIKFHENYVU',
     'XPLTDAOIKFZGHENYSRUBMCQWVJ',
     'TDSWAYXPLVUBOIKZGJRFHENMCQ',
     'BMCSRFHLTDENQWAOXPYVUIKZGJ',
     'XPHKZGJTDSENYVUBMLAOIRFCQW']
#存储密钥
c_k = [1,2,5,7,9,11,14,3,4,6,8,10,12,13]
#存储密文
c_t = 'BQKUTPVDKYUQVU'
#将密码器与密钥对应
c_list = [jwc[x-1] for x in c_k]
#转动密码器以还原密文
for i in range(len(c_t)):
    index = c_list[i].find(c_t[i])
    c_list[i] = c_list[i][index:]+c_list[i][:index]
#循环输出各列的信息，寻找符合的一项即可
for i in range(26):
    row = []
    for j in range(14):
        row.append(c_list[j][i])
    print "%dth row passwd is:%s"%(i,''.join(row))