f=open("./flag.enc","r")
flag_enc=f.read()
f.close()
flag=""
flag_enc_bin=""
c=0
for i in range(len(flag_enc)):
    flag_enc_bin+=bin(ord(flag_enc[i]))[2:].rjust(8,"0")
len_enc_bin=len(flag_enc_bin)
#print flag_enc_bin
for i in range(len_enc_bin/9):
    flag+=chr(int(flag_enc_bin[i*9:i*9+9],2))
print flag