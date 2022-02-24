hexadecimalcontrast = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'a':'1010',
        'b':'1011',
        'c':'1100',
        'd':'1101',
        'e':'1110',
        'f':'1111',
        }

def Binxor(string1,string2):
    "If the length is different, only the short one is returned."
    strlen = 0
    xorstr = ""
    if len(string1) > len(string2):
        strlen = len(string2)
    else:
        strlen = len(string1)
    for i in range(strlen):
        if string1[i] == string2[i]:
            xorstr += '0'
        else:
            xorstr += '1'
    return xorstr

def BinToStr(strbin):
    "Turn the binary string to a ASCII string"
    strten = ""
    for i in range(len(strbin)//8):
        num = 0
        test = strbin[i*8:i*8+8]
        for j in range(8):
            num += int(test[j])*(2**(7-j))
        strten += chr(num)
    return strten

def Textxor(string,num):
    "A different or a string and number"
    xorstr = ""
    if int == type(num):
        for i in string:
            xorstr += chr(ord(i) ^ num)
        return xorstr
    else:
        return -1

def HexToBin(string):
    "Convert sixteen to binary"
    Binstring = ""
    string = string.lower()
    for i in string:
        try:
            Binstring += hexadecimalcontrast[i]
        except:
            return -1
    return Binstring

def StrToHex(string):
    "Converts a string to HEX"
    hexStr = ''
    for i in string:
        tmp = str(hex(ord(i)))
        if len(tmp) == 3:
            hexStr += tmp.replace('0x','0')
        else:
            hexStr += tmp.replace('0x','')
    return hexStr

def NumToBin(number):
    tmp = str(hex(number))
    hexStr = ''
    tmp = tmp.replace('0x','')
    hexStr = '0'*(2-len(tmp)) + tmp
    hexStr = HexToBin(hexStr)
    hexStr = hexStr[2:]
    return hexStr
    
if "__main__" == __name__:
    print(Binxor(HexToBin('89504E470D0A1A0A0000000D'),HexToBin('0C6746601FC907F586867B48')))