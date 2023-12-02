#!/usr/bin/python3
import sys

tl_dict = {
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
        '1' : '1',
        '2' : '2',
        '3' : '3',
        '4' : '4',
        '5' : '5',
        '6' : '6',
        '7' : '7',
        '8' : '8',
        '9' : '9'
        }

def inner_loop(line):
    try:
        o = [c for c in line if (ord(c) <= 57)]
        return int(o[0] + o[-2])
    except IndexError:
        return 0

def part_one(input):
    total = 0
    for line in input.readlines():
        total += inner_loop(line)
    return total

def part_two(input):
    total = 0
    for line in input.readlines():
        realstr = ''
        for i in range(len(line)):
            for k in tl_dict.keys():
                if line[i:].startswith(k):
                    realstr += tl_dict[k]
        total += int(realstr[0] + realstr[-1])
    return total
