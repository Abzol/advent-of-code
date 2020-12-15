class machine:
    def __init__(self, input):
        self.accumulator = 0
        self.code = input.readlines()
        self.pc = 0
    def run_line(self, line):
        try:
            instruction, value = self.code[line].split()
            if instruction == 'nop':
                return line + 1
            if instruction == 'acc':
                self.accumulator += int(value)
                return line + 1
            if instruction == 'jmp':
                return line + int(value)
        except IndexError:
            return -1 #terminated
    def find_loop(self):
        exec_lines = set()
        old_pc = self.pc
        while (self.pc not in exec_lines and self.pc != -1):
            exec_lines.add (self.pc)
            old_pc = self.pc
            self.pc = self.run_line(self.pc)
            if (self.pc == -1):
                return -1 #didn't loop
        return old_pc
    def apply_patch(self, line):
        instruction, value = self.code[line].split()
        if instruction == 'jmp':
            self.code[line] = f'nop {value}'
        if instruction == 'nop':
            self.code[line] = f'jmp {value}'
    def find_solution(self):
        backup = self.code
        edit_line = 0
        looped = self.find_loop()
        while (looped != -1):
            self.accumulator = 0
            self.pc = 0
            self.apply_patch(edit_line)
            looped = self.find_loop()
            self.apply_patch(edit_line)
            edit_line += 1

def ver_one(input):
    console = machine(input)
    console.find_loop()
    return console.accumulator

def ver_two(input):
    console = machine(input)
    console.find_solution()
    return console.accumulator