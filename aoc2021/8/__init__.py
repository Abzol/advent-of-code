import sys

class Segment():
    def __init__(self, wires, outputs):
        self.wires = [x for x in wires.split()]
        self.outputs = [x for x in outputs.split()]
        self.mapping = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None}
    def solve(self):
        c_235 = []
        for wire in self.wires:
            if len(wire) == 2:
                c_one = wire
            if len(wire) == 3:
                c_seven = wire
            if len(wire) == 4:
                c_four = wire
            if len(wire) == 5:
                c_235.append(wire)
        self.mapping['a'] = [x for x in c_seven if x not in c_one][0] # guaranteed from intersection of 7 and 1
        for number in c_235:
            horizontals = ''
            for c in number:
                if c != self.mapping['a'] and all([c in c_235[0], c in c_235[1], c in c_235[2]]): #returns middle and bottom center lines
                    horizontals += c
        self.mapping['d'] = list(set(c_four) & set(horizontals))[0] # 4 and 235 shares only center middle line
        self.mapping['g'] = list(set(horizontals) - set(self.mapping['d']))[0] # 235 without 7 or 4 is bottom center
        self.mapping['b'] = list(set(c_four) - set(self.mapping['a'] + self.mapping['d']) - set(c_one))[0] # top left part of 4 guaranteed now
        for number in c_235:
            chars = set([x for x in number])
            chars = chars - set(self.mapping['a'] + self.mapping['d'] + self.mapping['g']) # get only vertical segments
            if chars != set(c_one): #if we arent looking at 3
                if self.mapping['b'] in chars:
                    self.mapping['f'] = list(chars - set(self.mapping['b']))[0] # guaranteed bottom right segment
                    self.mapping['c'] = list(set(c_one) - set(self.mapping['f']))[0] # and top right
                else:
                    c_two = chars
        self.mapping['e'] = list(set(c_two) - set(self.mapping['c']))[0] #last segment
    def get_solved_output(self):
        r = ''
        for digit in self.outputs:
            td = set(''.join([self.mapping[w] for w in digit]))
            outvals = {'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9', 'abcefg': '0'}
            for k, v in outvals.items():
                if td == set(k):
                    r += v
        return r

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
    for segment in segments:
        segment.solve() # solve all nodes :>
    t = 0
    return(''.join([segments[0].mapping[x] for x in segments[0].outputs[0]]))