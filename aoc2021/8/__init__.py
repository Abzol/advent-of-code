import sys

class Segment():
    def __init__(self, wires, outputs):
        self.wires = [x for x in wires.split()]
        self.outputs = [x for x in outputs.split()]
        self.BITS = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32, 'g': 64}
        self.connections = {'a': 127, 'b': 127, 'c': 127, 'd': 127, 'e': 127, 'f': 127, 'g': 127}
    def solve(self):
        print(self.wires)
        print(self.outputs)
        for wire in self.wires + self.outputs:
            pattern = sum([self.BITS[x] for x in wire])
            if len(wire) == 2: # out segments: 'cf' (1)
                for w in 'abdeg':
                    self.connections[w] = self.connections[w] & (127-pattern)
                for w in 'cf':
                    self.connections[w] = self.connections[w] & pattern
            if len(wire) == 3: # out segments: 'acf' (7)
                for w in 'bdeg':
                    self.connections[w] = self.connections[w] & (127-pattern)
                for w in 'acf':
                    self.connections[w] = self.connections[w] & pattern
            if len(wire) == 4: # out segments 'bcdf' (4)
                for w in 'aeg':
                    self.connections[w] = self.connections[w] & (127-pattern)
                for w in 'bcdf':
                    self.connections[w] = self.connections[w] & pattern
            if len(wire) == 5: # out segments 'acdeg' (2), 'acdfg' (3), or 'abdfg' (5):
                pass
            if len(wire) == 6: # out segments 'abdefg' (6), 'abcdfg' (9), or 'abcefg' (0):
                pass
            # 'abcdefg' (8) gives no useful information


def ver_one(input):
    lines = input.readlines()
    segments = []
    for line in lines:
        wires, outputs = line.split('|')
        segments.append(Segment(wires, outputs))
    t = 0
    for segment in segments:
        for output in segment.outputs:
            if len(output) in [2, 3, 4, 7]:
                t += 1
    return t

def ver_two(input):
    lines = input.readlines()
    segments = []
    for line in lines:
        wires, outputs = line.split('|')
        segments.append(Segment(wires, outputs))
    segments[0].solve()
    return segments[0].connections
    