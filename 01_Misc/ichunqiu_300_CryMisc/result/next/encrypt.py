# -*- coding:utf8 -*-
from base64 import *

s=open('flag.jpg','rb').read()
s='-'.join(map(b16encode,list(s)))
s=map(''.join,zip(*(s.split('-'))))
with open('first','wb') as f:
    f.write(b16decode(s[0]))
with open('second','wb') as f:
    f.write(b16decode(s[1]))