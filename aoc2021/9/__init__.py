import sys

def ver_one(input):
    heightmap = []
    for line in input.readlines():
        heightmap.append([int(x) for x in line.rstrip()])
    t = 0
    for y, row in enumerate(heightmap):
        for x, val in enumerate(row):
            adjacent = []
            if x > 0:
                adjacent.append(heightmap[y][x-1])
            if y > 0:
                adjacent.append(heightmap[y-1][x])
            if x < len(row)-1:
                adjacent.append(heightmap[y][x+1])
            if y < len(heightmap)-1:
                adjacent.append(heightmap[y+1][x])
            if val < min(adjacent):
                t += (val+1) 
    return t

# not a pure function, this edits heightmap
def floodfill(heightmap, x, y, v):
    size = 0
    if heightmap[y][x] != -1:
        size += 1
        heightmap[y][x] = v
        if x > 0:
            size += floodfill(heightmap, x-1, y, v)
        if y > 0:
            size += floodfill(heightmap, x, y-1, v)
        if x < len(heightmap[y])-1:
            size += floodfill(heightmap, x+1, y, v)
        if y < len(heightmap)-1:
            size += floodfill(heightmap, x, y+1, v)
    return size

def ver_two(input):
    heightmap = []
    for i, line in enumerate(input.readlines()):
        heightmap.append([])
        for x in line.rstrip():
            heightmap[i].append(0 if int(x) < 9 else -1)
    sizes = []
    for y, line in enumerate(heightmap):
        for x, v in enumerate(heightmap[y]):
            if v != -1:
                sizes.append(floodfill(heightmap, x, y, -1))
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]