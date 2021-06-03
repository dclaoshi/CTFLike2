# Source Generated with Decompyle ++
# File: __main__hello__.pyc (Python 2.7)
import sys
from hashlib import sha256 
import dis
import multiprocessing 
import UserList

def encrypt_string(s): 
    new_str = []
    for (index , c) in enumerate(s): 
        if index == 0:
            new_str.append(rot_chr(c, 10))
            continue
        new_str.append(rot_chr(c, ord(new_str[index - 1]))) 
    return ''.join(new_str)

def rot_chr(c, amount):
    return chr(((ord(c) - 33) + amount) % 94 + 33)

SECRET = 'w*0;CNU[\\gwPWk}3:PWk"#&:ABu/:Hi,M' 
if encrypt_string(sys.argv[1]) == SECRET:
    print 'Yup' 
else:
    print 'Nope'
