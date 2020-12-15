#!/usr/bin/python3
import sys

class IntcodeComputer:
    def readOp(self):
        try:
            self.ops[self.code[self.pc]]() #call function according to ops[]
        except KeyError:
            print("No opcode %d found" % self.code[self.pc])
            sys.exit()

    def opAdd(self):
        self.code[self.code[self.pc+3]] = self.code[self.code[self.pc+1]] + self.code[self.code[self.pc+2]]
        self.pc += 4

    def opMult(self):
        self.code[self.code[self.pc+3]] = self.code[self.code[self.pc+1]] * self.code[self.code[self.pc+2]]
        self.pc += 4

    def opExit(self):
        print(self.code[0])
        sys.exit()

    def run(self):
        while (self.pc < len(self.code)):
            self.readOp()

    def __init__(self, code):
        self.code = [int(i) for i in code] #translates everything to int
        self.pc = 0
        self.ops = {
                 1 : self.opAdd,
                 2 : self.opMult,
                99 : self.opExit
                }

if __name__ == "__main__":
    with open(sys.argv[-1]) as f:
        ic = IntcodeComputer(f.read().split(','))
        ic.run()
