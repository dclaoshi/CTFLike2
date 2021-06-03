#!/usr/bin/env python
#-*- coding: utf-8 -*-

f=open('myheart.txt','r')
x=list(f.readlines())
f.close()
listvalues=[]
indexlist=[]
for i in xrange(len(x)):
    d=x[i].split()[1].split('/')[0].split('-') #提取前后两个数
    flag=True
    for kline in listvalues:
        if (int(d[0])>=kline[0] and int(d[1])<=kline[1]):#若数在已存在的列表中，则取消存储
            flag=False
            break
    if flag:
        listvalues.append((int(d[0]),int(d[1])))#存储
        indexlist.append(i) #存储原顺序，以得到文件名

sortedpos=sorted([xx[0] for xx in listvalues]) #排序

fresult=open('resultx.png','wb')
fresult.write('89504E470D0A1A0A0000000D49'.decode('hex')) #写入png头，共13个字节
for i in xrange(len(sortedpos)):
    index=0
    for searchnums in listvalues:
        if(sortedpos[i]==searchnums[0]): #在存储的范围列表中找到位置序号
            break
        else:
            index+=1
    f=open('LoiRLUoq(%d)'%(indexlist[index]),'rb') #打开文件
    if(i!=len(sortedpos)-1):
        fresult.write(f.read()[:sortedpos[i+1]-sortedpos[i]])
    else:
        fresult.write(f.read())    
    f.close()
fresult.close()
print '执行完毕，请查看图片得到key'