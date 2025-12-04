from collections import Counter

def part_one(puzzle):
    values_left = []
    values_right = []
    try:
        for line in puzzle.readlines():
            a, b = line.split()
            values_left.append(int(a))
            values_right.append(int(b))
    except ValueError:
        pass
    values_left.sort()
    values_right.sort()
    total = 0
    for pair in zip(values_left, values_right):
        total = total + abs(pair[0] - pair[1])
    return total

def part_two(puzzle):
    values_left = []
    values_right = []
    try:
        for line in puzzle.readlines():
            a, b = line.split()
            values_left.append(int(a))
            values_right.append(int(b))
    except ValueError:
        pass
    counts = Counter(values_right)
    total = 0
    for x in values_left:
        total += x * counts[x]
    return total
