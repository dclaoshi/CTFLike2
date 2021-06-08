# -*- coding:utf8 -*-
from Crypto.Cipher import AES

s=open('next.zip','rb').read()
BS=16
pad_len=BS-len(s)%BS
padding=chr(pad_len)*pad_len
s+=padding

key='我后来忘了'
n=0x48D6B5DAB6617F21B39AB2F7B14969A7337247CABB417B900AE1D986DB47D971
e=0x10001
m=long(key.encode('hex'),16)
c=pow(m,e,n)
c='0{:x}'.format(c).decode('hex')
with open('RSA.encrypt','wb') as f:
    f.write(c)

obj=AES.new(key,AES.MODE_ECB)
with open('AES.encryt','wb') as f:
    f.write(obj.encrypt(s))