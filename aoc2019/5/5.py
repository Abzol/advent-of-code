#!/usr/bin/python3
import intcodeComputer
import sys

if __name__ == "__main__":
    with open(sys.argv[-1]) as f:
        ic = intcodeComputer.IntcodeComputer(f.read().split(','))
        ic.run()
