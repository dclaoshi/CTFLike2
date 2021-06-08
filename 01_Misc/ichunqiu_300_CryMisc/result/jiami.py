# -*- coding:utf8 -*-

import pyminizip
from hashlib import md5
import os
          
def create(files, zfile):
    password = os.urandom(15)
    password = md5(password).hexdigest()
    pyminizip.compress_multiple(files, zfile, password, 0)
    pass
      
if __name__ == '__main__':
    files = ['jiami.py','gogogo.zip']
    zfile = 'crypto.zip'
    create(files, zfile)