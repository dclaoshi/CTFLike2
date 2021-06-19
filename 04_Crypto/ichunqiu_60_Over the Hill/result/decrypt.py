#!/usr/bin/env python
#-*- coding: utf-8 -*-

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_{}"

matrix = [54,53,28,20,54,15,12,7,32,14,24,5,63,12,50,52,63,59,40,18,55,33,17,3,63,34,5,4,56,10,53,16,35,43,45,53,12,42,35,37,20,59,42,10,46,56,12,61,26,39,27,59,44,54,23,56,32,31,56,47,31,2,29,41]

ciphertext = "7Nv7}dI9hD9qGmP}CR_5wJDdkj4CKxd45rko1cj51DpHPnNDb__EXDotSRCP8ZCQ"

plaintext = []

for cipherchar in ciphertext:
    alphabet_index = alphabet.index(cipherchar)
    origin_index = matrix.index(alphabet_index)
    originchar = alphabet[origin_index-1] 
    plaintext.append(originchar)

print "".join(plaintext)