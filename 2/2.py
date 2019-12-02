#!/usr/bin/python3
import sys

def opAdd(code, x, y, d):
    code[d] = int(code[x]) + int(code[y])

def opMult(code, x, y, d):
    code[d] = int(code[x]) * int(code[y])

def readOp(code, pos):
    if int(code[pos]) == 1:
        opAdd(code, int(code[pos+1]), int(code[pos+2]), int(code[pos+3]))
    elif int(code[pos]) == 2:
        opMult(code, int(code[pos+1]), int(code[pos+2]), int(code[pos+3]))
    elif int(code[pos]) == 99:
        print(code[0])
        sys.exit()
    else:
        raise SyntaxError

if __name__ == "__main__":
    with open(sys.argv[-1]) as f:
        codes = f.read().split(",")
        for index in range(len(codes)):
            readOp(codes, index*4)
