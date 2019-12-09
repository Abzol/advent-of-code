#!/usr/bin/python3
import sys

class IntcodeComputer:
    #left-pads a list with leading zeroes until specified length
    def padModes(self, modes, length):
        return (length * [0] + modes)[-length:]

    def readArgument(self, mode, argument):
        try:
            if (mode == 1):
                return argument
            else:
                return self.code[argument]
        except IndexError:
            return self.code[argument]

    def parseArguments(self, modes, paramCount):
        params = []
        modes = self.padModes(modes, paramCount)
        for i in range(1, len(modes) + 1):
            params.append(int(self.readArgument(modes[-i], self.code[self.pc+i])))
        return params

    def readOp(self):
        opcode = [int(x) for x in str(self.code[self.pc])]
        try:
            opcode[-2] = 10 * opcode[-2] + opcode[-1]
            del opcode[-1]
        except IndexError:
            pass #single-digit opcode will IndexError; this is expected
        try:
            self.ops[opcode[-1]](opcode[:-1]) #calls opcode[-1], with all previous elements as arguments OR empty list
            # opcode 1 will thus pass as self.opAdd([]), while opcode 1001 will pass as self.opAdd([1,0])
        except KeyError:
            print("No opcode %d found" % self.code[self.pc])
            sys.exit()

    def opAdd(self, modes):
        x, y, _ = self.parseArguments(modes, 3)
        self.code[self.code[self.pc+3]] = x + y
        self.pc += 4

    def opMult(self, modes):
        x, y, _ = self.parseArguments(modes, 3)
        self.code[self.code[self.pc+3]] = x * y
        self.pc += 4

    def opMov(self, modes):
        try:
            if len(self.inputs) > 0:
                self.code[self.code[self.pc+1]] = self.inputs.pop(0)
                self.pc += 2
                return
        except TypeError:
            pass
        self.code[self.code[self.pc+1]] = input("Awaiting input... ")
        self.pc += 2

    def opPrint(self, modes):
        print(self.code[self.code[self.pc+1]])
        self.pc += 2

    def opJumpIfTrue(self, modes):
        x, y = self.parseArguments(modes, 2)
        if (x != 0):
            self.pc = y
        else:
            self.pc += 3

    def opJumpIfFalse(self, modes):
        x, y = self.parseArguments(modes, 2)
        if (x == 0):
            self.pc = y
        else:
            self.pc += 3

    def opLessThan(self, modes):
        x, y, _ = self.parseArguments(modes, 3)
        if (x < y):
            self.code[self.code[self.pc+3]] = 1
        else:
            self.code[self.code[self.pc+3]] = 0
        self.pc += 4
    
    def opEquals(self, modes):
        x, y, _ = self.parseArguments(modes, 3)
        if (x == y):
            self.code[self.code[self.pc+3]] = 1
        else:
            self.code[self.code[self.pc+3]] = 0
        self.pc += 4

    def opExit(self, modes):
        sys.exit()

    def run(self):
        while (self.pc < len(self.code)):
            self.readOp()

    def __init__(self, code, inputs=None):
        self.code = [int(i) for i in code] #translates everything to int
        self.pc = 0
        self.ops = {
                 1 : self.opAdd,
                 2 : self.opMult,
                 3 : self.opMov,
                 4 : self.opPrint,
                 5 : self.opJumpIfTrue,
                 6 : self.opJumpIfFalse,
                 7 : self.opLessThan,
                 8 : self.opEquals,
                99 : self.opExit
                }
        self.inputs = inputs

if __name__ == "__main__":
    print("this is a module; import it")
