#!/usr/bin/env python
import random
import base64

def KeyGenerate():
    random.seed(10)
    keyseed = ''
    for i in range(12):
        x = random.randint(32, 127)
        keyseed += chr(x)
    return base64.b64encode(keyseed.encode('utf-8')).decode('utf-8')

def dec(key):
    count = 0
    f = open('encrypted', 'rb')
    f1 = open('decrypted', 'wb')
    for now in f:
        for nowByte in now:
            newByte = nowByte ^ ord(key[count % len(key)])
            count += 1
            f1.write(bytes([newByte]))

if __name__ == '__main__':
    key = KeyGenerate()
    dec(key)