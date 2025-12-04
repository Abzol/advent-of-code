def part_one(f):
    d = f.read()
    ranges = d.strip().split(',')
    invalid = []
    for r in ranges:
        lo, hi = r.split('-')
        for i in range(int(lo), int(hi)+1):
            v = str(i)
            if (len(v)%2 == 0):
                if (v[len(v)//2:] == v[:len(v)//2]):
                    invalid.append(i)
    return sum(invalid)

import re

def part_two(f):
    d = f.read()
    ranges = d.strip().split(',')
    invalid = []
    for r in ranges:
        lo, hi = r.split('-')
        for i in range(int(lo), int(hi)+1):
            v = str(i)
            pattern = re.compile('^(.*?)\\1+$')
            if re.search(pattern, v):
                invalid.append(i)
    return sum(invalid)
