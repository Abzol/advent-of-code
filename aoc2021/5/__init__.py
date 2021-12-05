import sys
import re
from math import copysign

class Ventline():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def is_aligned(self):
        return (self.x1 == self.x2 or self.y1 == self.y2)
    def get_coverage(self):
        l = abs(self.x2 - self.x1) or abs(self.y2 - self.y1)
        x = self.x1
        y = self.y1
        for i in range(l+1):
            yield f'{int(x)},{int(y)}'
            if self.x1 != self.x2:
                x = x + copysign(1, (self.x2-self.x1))
            if self.y1 != self.y2:
                y = y + copysign(1, (self.y2-self.y1))

def ver_one(input):
    lines = input.readlines()
    ventpattern = {}
    for line in lines:
        data = [int(x) for x in re.split('->|,', line)]
        vents = Ventline(data[0], data[1], data[2], data[3])
        if vents.is_aligned():
            for x in vents.get_coverage():
                if x not in ventpattern:
                    ventpattern[x] = 1
                else:
                    ventpattern[x] = ventpattern[x] + 1
    t = 0
    for k in ventpattern:
        if ventpattern[k] > 1:
            t+=1
    return t

def ver_two(input):
    lines = input.readlines()
    ventpattern = {}
    for line in lines:
        data = [int(x) for x in re.split('->|,', line)]
        vents = Ventline(data[0], data[1], data[2], data[3])
        for x in vents.get_coverage():
            if x not in ventpattern:
                ventpattern[x] = 1
            else:
                ventpattern[x] = ventpattern[x] + 1
    t = 0
    for k in ventpattern:
        if ventpattern[k] > 1:
            t+=1
    return t