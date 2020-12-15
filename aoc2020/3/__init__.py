#!/usr/bin/python3
import sys
from math import prod

def traverse_map(trees, right, down):
    x = 0
    y = 0
    count = 0
    try:
        while (y < len(trees)):
            x = (x + right) % len(trees[0].rstrip()) #too lazy to check if input file is LF or CRLF
            y = y + down
            if trees[y][x] == '#':
                count += 1
    except IndexError:
        pass
    return count

def ver_one(input):
    return traverse_map(input.readlines(), 3, 1)

def ver_two(input):
    trees = input.readlines()
    slopes = [traverse_map(trees, 1, 1),
              traverse_map(trees, 3, 1),
              traverse_map(trees, 5, 1),
              traverse_map(trees, 7, 1),
              traverse_map(trees, 1, 2),]
    return prod(slopes)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        try:
            if (sys.argv[2] == "1"):
                print(ver_one(f))
            elif (sys.argv[2] == "2"):
                print(ver_two(f))
            else:
                print("No such answer")
        except IndexError:
            print("Missing answer request")