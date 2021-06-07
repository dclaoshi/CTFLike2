f=open('blue_monday','r')
flag=''
s=f.read()
length=len(s)
i=0
while i<length:
    if ord(s[i])==0x64:
        flag+=s[i-1]
    i=i+1
print flag