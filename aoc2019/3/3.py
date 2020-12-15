#!/usr/bin/python3

#dont look at the commit history for this file

import sys

def readwire(wire, output):
    pos = (0,0)
    steps = 0
    def tracewire(direction):
        for i in range(1,int(step[1:]) + 1):
            nonlocal pos, steps, output
            steps += 1
            pos = (pos[0] + direction[0], pos[1] + direction[1])
            if pos not in output:
                output[pos] = steps
 
    for step in wire:
        if step[0] == "R":
            tracewire((1,0))
        elif step[0] == "U":
            tracewire((0,-1))
        elif step[0] == "L":
            tracewire((-1,0))
        elif step[0] == "D":
            tracewire((0,1))

if __name__ == "__main__":
    wire1 = {} #set instead of list improved runtime by a factor of 3804.25
    wire2 = {} #they're now dicts cause we need to keep steps also
    with open(sys.argv[-1]) as f:
        wire = f.readline().split(',') # read the first wire
        readwire(wire, wire1)
        wire = f.readline().split(',') # read the second wire
        readwire(wire, wire2)
    collisions = set()
    for key in wire1:
        if key in wire2:
            collisions.add(wire1[key]+wire2[key])
    print(min(collisions))
