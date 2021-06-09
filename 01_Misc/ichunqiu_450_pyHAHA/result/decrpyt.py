from os import urandom

def generate(m, k):
    result = 0
    for i in bin(m ^ k)[2:]:
        result = result << 1
        if int(i):
            result = result ^ m ^ k
        if result >> 256:
            result = result ^ P
            continue
    return result

def convert(string):
    return int(string.encode('hex'), 16)


P = 0x10000000000000000000000000000000000000000000000000000000000000425L
flag1 = 'ThIs_Fl4g_Is_Ri9ht'
flag2 = 'Hey_Fl4g_Is_Not_HeRe'
encrypt1 = open('encrypt.txt', 'r').read()
encrypt2 = 0xec8d57d820ad8c586e4be0122b442c871a3d71cd8036c45083d860caf1793ddc
encrypt3 = 0xc40a0be335babcfbd8c47aa771f6a2ceca2c8638caa5924da58286d2a942697e
key3 = encrypt3 ^ convert(flag2)
key2 = encrypt2 ^ convert(flag1)
print('Found key2:',key2)
print('Found key3:',key3)

tmp = key3 - 233333333333L
for i in range(0,255):
    tmp = generate(tmp,0)
seed = tmp ^ key2
print 'Found seed:',seed
print 'use seed generate key3:',generate(key2,seed)+233333333333L

tmp = key2 - 233333333333L
for i in range(0,255):
    tmp = generate(tmp,0)
key1 = tmp ^ seed
print 'Found key1:',key1
print 'use key1 generate key2:',generate(key1,seed)+233333333333L

result = eval(hex(int(encrypt1,2))[:-1]) ^ eval('0x'+hex(key1)[2:-1]*22)
data = open('data.txt', 'w')
data.write(bin(result)[2:])
data.close()