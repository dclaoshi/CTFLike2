import z3

outBin = '100001010011011100001000001001110001001011000011000111011111111110000110100001100111101101000101'
def numcc(keytLen):
    p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30 = z3.BitVecs('p0 p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 p11 p12 p13 p14 p15 p16 p17 p18 p19 p20 p21 p22 p23 p24 p25 p26 p27 p28 p29 p30',1)
    s = z3.Solver()
    for i in range(keytLen):
        ceshi =  outBin[i:keytLen+i+1]
        print ceshi
        ming = ''
        for i in range(keytLen):
            if ceshi[i] == '1':
                ming += 'p' + str(i) + '+'
            else:
                pass
        ming = ming[0:-1] + '==' + str(ceshi[-1])
        #print ming    
        s.add(eval(ming))
    s.add()
    print s
    if s.check() == sat:
        print s.model()
    #print s.check()

for i in range(2,30):
    numcc(i)
    #pass
    #numcc(6)