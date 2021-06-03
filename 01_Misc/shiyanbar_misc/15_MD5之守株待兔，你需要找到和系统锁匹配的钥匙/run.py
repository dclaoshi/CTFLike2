#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-11
@description : MD5之守株待兔，你需要找到和系统锁匹配的钥匙
@Update date :   
"""  
import time
import requests
import hashlib

currTime = int(time.time())
print currTime

response = requests.get("http://ctf5.shiyanbar.com/misc/keys/keys.php?key=" + str(currTime))
print response.text