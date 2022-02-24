# coding:utf-8
import re
import binascii
n = 115130
result = ''
fina = ''
file = open('flag-woody.mp3','rb')
while n < 2222222 :
    file.seek(n,0)
    n += 1044
    file_read_result = file.read(1)
    read_content = bin(ord(file_read_result))[-1]
    result = result + read_content
print(result)
textArr = re.findall('.{'+str(8)+'}', result)
print(textArr)
textArr.append(result[(len(textArr)*8):])
print(textArr)

for i in textArr:
    fina = fina + hex(int(i,2))[2:].strip('\n')

fina = fina#.decode('hex')
print (fina)