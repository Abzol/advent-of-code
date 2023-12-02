#!/usr/bin/python3
import re
from functools import reduce

limits = {
        'red' : 12,
        'green' : 13,
        'blue' : 14
        }

def part_one(f):
    total = 0
    for line in f.readlines():
        game = re.split(':|;', line)
        valid = True
        for shown in game[1:]:
            cubes = shown.split(',')
            for color in cubes:
                num, col = color.strip().split(' ')
                if int(num) > limits[col]:
                    valid = False
        if valid:
            total += int(game[0][5:])
    return total

def part_two(f):
    total = 0
    for line in f.readlines():
        game = re.split(':|;', line)
        minimum = {}
        for shown in game[1:]:
            cubes = shown.split(',')
            for color in cubes:
                num, col = color.strip().split(' ')
                if col not in minimum:
                    minimum[col] = int(num)
                else:
                    if int(num) > minimum[col]:
                        minimum[col] = int(num)
        power = reduce(lambda x, y: x*y, minimum.values())
        total += power
    return total
