#!/usr/bin/python3
import sys
import importlib

if __name__ == "__main__":
    if (len(sys.argv) == 3):
        with open(f'{sys.argv[1]}/input') as f:
            answer = importlib.import_module(sys.argv[1])
            if (sys.argv[2] == "1"):
                print(answer.part_one(f))
            elif (sys.argv[2] == "2"):
                print(answer.part_two(f))
            else:
                print("No such answer")
    else:
        print("Missing arguments")
