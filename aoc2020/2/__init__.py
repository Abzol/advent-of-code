#!/usr/bin/python3
import sys

def ver_one(input):
    total = 0
    for line in input.readlines():
        limit, letter, password = line.split()
        limit = limit.split('-')
        count = 0
        for c in password:
            if (c == letter[0]):
                count += 1
        if (int(limit[0]) <= count and int(limit[1]) >= count):
            total += 1
    return total

def ver_two(input):
    total = 0
    for line in input.readlines():
        positions, letter, password = line.split()
        positions = positions.split('-')   
        if (bool(password[int(positions[0])-1] == letter[0]) != bool(password[int(positions[1])-1] == letter[0])):
            total += 1
    return total

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