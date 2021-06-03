#-*- coding:latin-1 -*-

import chardet

f = open("2.eml","r")
content = f.read().strip()
#print content
content = content.decode("base64")
print chardet.detect(content)
f.close()

f = open("result.txt","wb+")
f.write(content[3:])