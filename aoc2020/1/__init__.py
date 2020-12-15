#!/usr/bin/python3
import sys

def ver_one(input):
    numbers = input.readlines()
    for i in numbers:
        for j in numbers:
            if (int(i) + int(j) == 2020):
                return int(i)*int(j)

def ver_two(input):
    numbers = input.readlines()
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if (int(i) + int(j) + int(k) == 2020):
                    return int(i) * int(j) * int(k)