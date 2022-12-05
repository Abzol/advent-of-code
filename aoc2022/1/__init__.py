import itertools

def part_two(f):
    return max([sum([int(x) for x in cals]) for empty, cals in itertools.groupby(f.readlines(), lambda z: z == '\n') if not empty])

def part_two(f):
    return sum(sorted([sum([int(x) for x in cals]) for empty, cals in itertools.groupby(f.readlines(), lambda z: z == '\n') if not empty])[-3:])
