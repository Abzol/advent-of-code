#!/usr/bin/python3
import sys

def ver_one(input):
    numbers = [int(x) for x in input.readlines()]
    t = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            t += 1
    return t

def ver_two(input):
    numbers = [int(x) for x in input.readlines()]
    t = 0
    for i in range(3, len(numbers)):
        if numbers[i] > numbers[i-3]:
            t += 1
    return t