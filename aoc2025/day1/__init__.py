def part_one(f):
    rot = 50
    hits = 0
    for line in f.readlines():
        if line.strip():
            dir = 1 if line.startswith('R') else -1
            val = int(line[1:])
            rot = (rot + (val * dir)) % 100
            if rot == 0:
                hits = hits + 1
    return hits

def part_two(f):
    rot = 50
    hits = 0
    for line in f.readlines():
        if line.strip():
            dir = 1 if line.startswith('R') else -1
            val = int(line[1:])
            for i in range(val):
                rot = (rot + dir) % 100
                if rot == 0:
                    hits = hits + 1 
    return hits
