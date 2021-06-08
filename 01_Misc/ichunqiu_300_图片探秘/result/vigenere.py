#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author : darkN0te
@Create date : 2021年6月8日08:26:10
@description : 维吉尼亚免密相关
@Update date :
"""

"""
秘钥是6位，所以减去密文最前一位，
whlrs.Tsgw vt kcg xybs:xaxybs{W_Zf0j_o0fvxft}

"""

# 用一直明文先计算一波秘钥
def calc_yizhi_mingwen(miwen, mingwen):
    keys = []
    for i in range(len(miwen)):
        keys.append((ord(miwen[i]) - ord(mingwen[i]))%26)
    return keys

print calc_yizhi_mingwen("xybs", "flag")

def decrpyt(miwen, keys):
    print keys
    mingwen = []
    keys_index = 0
    keys_len = len(keys)
    for miwen_char in miwen:
        # a = 97 z = 122   A = 65 Z = 90
        miwen_char_ord = ord(miwen_char)
        if miwen_char_ord >= 97 and miwen_char_ord <= 122:
            mingwen_char = (miwen_char_ord%97 - keys[keys_index % keys_len]) % 26 + 97
            keys_index += 1
            mingwen.append(chr(mingwen_char))
        elif miwen_char_ord >= 65 and miwen_char_ord <= 90:
            mingwen_char = (miwen_char_ord%65 - keys[keys_index % keys_len]) % 26 + 65
            keys_index += 1
            mingwen.append(chr(mingwen_char))
        else:
            mingwen.append(miwen_char)
    return "".join(mingwen)

def burp_key(miwen):
    for x1 in range(26):
        for x2 in range(26):
            keys = [x1, x2, 18, 13, 1, 12]
            try:
                print decrpyt(miwen, keys)
            except Exception as e:
                print e
                pass

miwen = "whlrs.Tsgw vt kcg xybs:xaxybs{W_Zf0j_o0fvxft}"
burp_key(miwen)