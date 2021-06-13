#!/usr/bin/env python
# -*- coding: utf-8 -*-

ciphertext = "WvyVKT"
j = 1
for j in range(26):
    for i in ciphertext:
        print(chr(ord(i) - j), end='')
        j += 1
    print()