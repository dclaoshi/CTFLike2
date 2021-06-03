#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2021年5月31日17:07:20
@description : 培根解密
@Update date :   
"""  

dicc = {'AAAAA':'a','AAAAB':'b','AAABA':'c','AAABB':'d','AABAA':'e','AABAB':'f',
        'AABBA':'g','AABBB':'h','ABAAA':'i/j','ABAAB':'k','ABABA':'l','ABABB':'m',
        'ABBAA':'n','ABBAB':'o','ABBBA':'p','ABBBB':'q','BAAAA':'r','BAAAB':'s',
        'BAABA':'t','BAABB':'u/v','BABAA':'w','BABAB':'x','BABBA':'y','BABBB':'z'}
init = "bacoN is one of aMerICa'S sWEethEartS. it's A dARlinG, SuCCulEnt fOoD tHAt PaIRs FlawLE"
init = init.replace(' ','').replace('.','').replace(',','').replace("'",'')
l = len(init)
assert l%5 == 0
ans1=''
ans2=''
ans3 = []
ans4 = []
for i in init:
    if i.isupper():
        ans1 += 'A'
        ans2 += 'B'
    else:
        ans1 += 'B'
        ans2 += 'A'
for i in range(l//5):
    ans3 .append(ans1[i*5:i*5+5])
    ans4 .append(ans2[i*5:i*5+5])
print("first : " + ans1)
print("second : " + ans2)

try:
    for i in range(len(ans3)):
        ans3[i] = dicc[ans3[i]]
    print(''.join(ans3))
except:
    print("first error")
    
try:
    for i in range(len(ans4)):
        ans4[i] = dicc[ans4[i]]
    print(''.join(ans4))
except:
    print("second error")