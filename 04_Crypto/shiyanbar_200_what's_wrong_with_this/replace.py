import opcode 
import sys

opmapfile = sys.argv[1]

with open(opmapfile , "r") as fd: 
    opmap = {}
    for line in fd:
        print line 
        code, op = line.split() 
        op = op.replace("+", "_") 
        opmap[op] = int(code)

for k,v in opcode.opmap.items():
    op = k.replace("+", "_")
    if opmap.has_key("_".join((op, "A"))):
        op = "_".join((op, "A")) 
    opmap[op] = v

with open(opmapfile , "wt") as fd:
    for k,v in sorted(opmap.items(), key = lambda x: x[1]):
        fd.write("%-3s %s\n" % (v,k))