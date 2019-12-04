#! /usr/bin/python3

import sys
from itertools import groupby

def isIncrementing(x):
    digits = [int(d) for d in str(x)]
    for i in range(1, len(digits)):
        if digits[i] < digits[i-1]:
            return False
    return True

def hasDoubleDigits(x):
    digits = [int(d) for d in str(x)]
    for i in range(1, len(digits)):
        if digits[i] == digits[i-1]:
            return True
    return False

def hasUniqueDoubleDigits(x):
    if not hasDoubleDigits(x):
        return False
    digits = [int(d) for d in str(x)]
    groupedDigits = list(groupby(digits))
    groupSizes = [len(x) for x in groupedDigits]
    if 2 in groupSizes:
        print(x)
        return True
    return False

def isValidPassword(x):
    return isIncrementing(x) and hasUniqueDoubleDigits(x)

if __name__ == "__main__":
    low = int(sys.argv[1])
    high = int(sys.argv[2])
    span = range(low,high)
    validPasswords = filter(isValidPassword, span)
    print(len(list(validPasswords)))
