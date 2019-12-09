#!/usr/bin/python3
import intcodeComputer
from io import StringIO
import sys

if __name__ == "__main__":
    #sysout = sys.stdout
    #result = StringIO()
    #sys.stdout = result
    with open(sys.argv[-1]) as f:
        code = f.read().split(',')
        ic = intcodeComputer.IntcodeComputer(code, inputs=sys.argv[1:-1])
        ic.run()
