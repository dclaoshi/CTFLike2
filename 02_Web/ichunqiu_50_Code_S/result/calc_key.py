# -*- coding:utf8 -*-
import base64
import requests

import string

url = "http://e7cdc5935f8c4dadb1e189314dbac34a951b6c52726b47cd.changame.ichunqiu.com/fl3g_ichuqiu.php"

crypt = 'Y0o1dUJLC01N'
text = 'guest'
crypt = base64.b64decode(crypt)
rnd = crypt[0:4]
crypt = crypt[4:]
tmp = ''

for i in range(5):
    tmp += chr(ord(text[i]) + 10)

key = ''
for i in range(5):
    key += chr(ord(tmp[i]) ^ ord(crypt[i]))

cookies = []
system = 'system'
tt = ''

for i in range(6):
    tt += chr(ord(system[i]) + 10)

for i in '0123456789abcdef':        #这里为啥是"1-f"，因为md5最终返回的数值是16进制对应的字符是0~9 a~f,所以这里范围为这一段
    true_key = key + i
    tmp = ''
    for i in range(6):
        tmp += chr(ord(true_key[i]) ^ ord(tt[i]))
    cookies.append(base64.b64encode(rnd + tmp))
    
for i in cookies:
    cookie = {'user' : i}
    r = requests.session()
    result = r.get(url, cookies = cookie)   
    print result.text