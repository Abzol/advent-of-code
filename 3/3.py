#!/usr/bin/python3

# to anyone reading this; i really didnt like this assignment
# im sorry its so shitty code. i should have broken it into functions
# but i was too lazy

import sys

if __name__ == "__main__":
    wire1 = {} #set instead of list improved runtime by a factor of 3804.25
    wire2 = {} #they're now dicts cause we need to keep steps also
    with open(sys.argv[-1]) as f:
        pos = (0,0)
        wire = f.readline().split(',') # read the first wire
        steps = 0
        for step in wire:
            if step[0] == "R":
                for i in range(1,int(step[1:]) + 1):
                    steps += 1
                    pos = (pos[0] + 1, pos[1])
                    if pos not in wire1:
                        wire1[pos] = steps
            elif step[0] == "U":
                for i in range(1,int(step[1:]) + 1):
                    steps += 1
                    pos = (pos[0], pos[1] - 1)
                    if pos not in wire1:
                        wire1[pos] = steps
            elif step[0] == "L":
                for i in range(1,int(step[1:]) + 1):
                    steps += 1
                    pos = (pos[0] - 1, pos[1])
                    if pos not in wire1:
                        wire1[pos] = steps
            elif step[0] == "D":
                for i in range(1,int(step[1:]) + 1):
                    steps += 1
                    pos = (pos[0], pos[1] + 1)
                    if pos not in wire1:
                        wire1[pos] = steps
        pos = (0,0)
        wire = f.readline().split(',') # read the second wire
        steps = 0
        for step in wire:
            if step[0] == "R":
                for i in range(1,int(step[1:]) + 1):
                    steps += 1
                    pos = (pos[0] + 1, pos[1])
                    if pos not in wire2:
                        wire2[pos] = steps
            elif step[0] == "U":
                for i in range(1,int(step[1:]) + 1):
                    steps += 1
                    pos = (pos[0], pos[1] - 1)
                    if pos not in wire2:
                        wire2[pos] = steps
            elif step[0] == "L":
                for i in range(1,int(step[1:]) + 1):
                    steps += 1
                    pos = (pos[0] - 1, pos[1])
                    if pos not in wire2:
                        wire2[pos] = steps
            elif step[0] == "D":
                for i in range(1,int(step[1:]) + 1):
                    steps += 1
                    pos = (pos[0], pos[1] + 1)
                    if pos not in wire2:
                        wire2[pos] = steps
    collisions = set()
    for key in wire1:
        if key in wire2:
            collisions.add(wire1[key]+wire2[key])
    print(collisions)
    shortest = -1
    for i in wire2:
        dist = abs(i[0]) + abs(i[1])
        if (dist < shortest or shortest == -1):
            shortest = dist
    print(shortest)
