#!/usr/bin/python3
import intcodeComputer
import sys

if __name__ == "__main__":
    with open(sys.argv[-1]) as f:
        code = f.read().split(',')
        ic = intcodeComputer.IntcodeComputer(code)
        print(ic.run(inputs=sys.argv[1:-1]))
