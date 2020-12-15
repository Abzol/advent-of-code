#!/usr/bin/python3
import intcodeComputer
import sys
from itertools import permutations

if __name__ == "__main__":
    with open(sys.argv[-1]) as f:
        code = f.read().split(',')
        max_out = 0
        for phases in permutations([5, 6, 7, 8, 9]):
            amp_a = intcodeComputer.IntcodeComputer(code)
            amp_b = intcodeComputer.IntcodeComputer(code)
            amp_c = intcodeComputer.IntcodeComputer(code)
            amp_d = intcodeComputer.IntcodeComputer(code)
            amp_e = intcodeComputer.IntcodeComputer(code)
            amps = [amp_a, amp_b, amp_c, amp_d, amp_e]
            ret = 0
            last_out = None
            for i in range(len(amps)):
                ret = amps[i].run([phases[i], ret])
            while( all(not amp.halted() for amp in amps)):
                for amp in amps:
                    ret = amp.run([ret])
                if (ret != None):
                    last_out = ret
            if last_out > max_out:
                max_out = last_out
        print(max_out)
