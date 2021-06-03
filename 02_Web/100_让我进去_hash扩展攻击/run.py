#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-10
@description : 哈希长度攻击
@Update date :   
"""  

import hashpumpy

# def hashpump(hexdigest, original_data, data_to_add, key_length)
aaa = hashpumpy.hashpump("571580b26c65f306376d4f64e53cb5c7","admin","darkN0te",20)
print aaa
