#!/usr/bin/python3
import sys

def ver_one(input):
    commands = input.readlines()
    total_h = 0
    total_v = 0
    for command in commands:
        direction, amount = command.split()
        if direction == "forward":
            total_h += int(amount)
        if direction == "up":
            total_v -= int(amount)
        elif direction == "down":
            total_v += int(amount)
    return total_h * total_v

def ver_two(input):
    commands = input.readlines()
    total_h = 0
    total_v = 0
    aim = 0
    for command in commands:
        direction, amount = command.split()
        if direction == "forward":
            total_h += int(amount)
            total_v += aim * int(amount)
        if direction == "up":
            aim -= int(amount)
        elif direction == "down":
            aim += int(amount)
    return total_h * total_v