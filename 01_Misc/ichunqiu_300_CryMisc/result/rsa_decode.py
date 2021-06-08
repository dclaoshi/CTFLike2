#-*- coding: UTF-8 -*- 

import gmpy2
import binascii

q = 185783328357334813222812664416930395483
p = 177334994338425644535647498913444186659
e = 0x10001
n = 0x48D6B5DAB6617F21B39AB2F7B14969A7337247CABB417B900AE1D986DB47D971
d = gmpy2.invert(e, (p-1)*(q-1))
print d
# m = pow(c,d,n)

c_file = open("gogogo/RSA.encrypt", "rb")
c = binascii.hexlify(c_file.read())
c = int(c, 16)
m = gmpy2.powmod(c,d,n)
print m
print binascii.unhexlify(hex(m)[2:])