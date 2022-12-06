def part_one(f):
    data = f.readline()
    for seg in range(4,len(data)):
        if len(set(data[seg-4:seg])) == 4:
            return seg

def part_two(f):
    data = f.readline()
    for seg in range(14, len(data)):
        if len(set(data[seg-14:seg])) == 14:
            return seg
