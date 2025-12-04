#!/usr/bin/python3
import sys
import importlib
import aoc

if __name__ == "__main__":
    if (len(sys.argv) >= 4):
        fn = 'input'
        try:
            fn = sys.argv[4]
        except IndexError:
            pass
        with open(f'aoc{sys.argv[1]}/day{sys.argv[2]}/{fn}') as f:
            answer = importlib.import_module(f'aoc{sys.argv[1]}.day{sys.argv[2]}')
            if (sys.argv[3] == "1"):
                print(answer.part_one(f))
            elif (sys.argv[3] == "2"):
                print(answer.part_two(f))
            else:
                print("No such answer")
    else:
        print("Missing arguments")
