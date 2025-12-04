import sys

def ver_one(input):
    squid = []
    for line in input.readlines():
        squid.append([int(x) for x in line.rstrip()])
    # +1 all squid
    t = 0
    for i in range(100):
        for y in range(len(squid)):
            for x in range(len(squid[y])):
                squid[y][x] += 1
        
        done = True
        while (not done):
            done = True
            for y in range(len(squid)):
                for x in range(len(squid[y])):
                    if squid[y][x] >= 9 and squid[y][x] < 20:
                        squid[y][x] = 20
                        squid[y][x-1] += 1
                        squid[y][x+1] += 1
                        squid[y-1][x-1] += 1
                        squid[y-1][x] += 1
                        squid[y-1][x+1] += 1
                        squid[y+1][x-1] += 1
                        squid[y+1][x] += 1
                        squid[y+1][x+1] += 1
                        done = False
        for y in range(len(squid)):
            for x in range(len(squid[y])):
                if squid[y][x] >= 9:
                    squid[y][x] = 0
                    t += 1
    return t
            