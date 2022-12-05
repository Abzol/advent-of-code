import string

priority = dict(zip(string.ascii_letters, range(1, 53)))

def part_one(f):
    total = 0
    try:
        for line in f.readlines():
            itemcount = len(line.rstrip())
            a = set(line[:(itemcount//2)])
            b = set(line[(itemcount//2):])
            misplaced = a & b
            total += priority[misplaced.pop()]
    except KeyError:
        pass # end of file
    return total

def part_two(f):
    total = 0
    try:
        groups = list(zip(*[iter(f.readlines())]*3))
        for group in groups:
            uniq = set(group[0].rstrip()) & set(group[1].rstrip()) & set(group[2].rstrip())
            total += priority[uniq.pop()]
    except KeyError:
        pass # end of file
    return total
