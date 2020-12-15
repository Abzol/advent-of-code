#!/usr/bin/python3
import sys
from math import floor

def calculateFuelReq(mass):
    return max(floor(mass/3)-2,0) #max for 0 as lower bound

def calculateRecursiveFuelReq(mass):
    req = calculateFuelReq(mass)
    if req > 0:
        req += calculateRecursiveFuelReq(req) 
    return req

if __name__ == "__main__":
    with open(sys.argv[-1]) as f: #open the last argument
        total = 0
        #with no -r argument, calculate answer to part 1
        if sys.argv[1] != "-r":
            for module in f:
                total += calculateFuelReq(int(module))
        # give -r argument to calculate answer to part 2
        elif sys.argv[1] == "-r":
            for module in f:
                total += calculateRecursiveFuelReq(int(module))
        print(total)
