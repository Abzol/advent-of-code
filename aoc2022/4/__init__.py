from math import copysign

def part_one(f):
    # this is a rather strange way to solve it but i thought it was
    # mathematically interesting. the reasonable way to just compare the
    # start and end values directly is much more reasonable i think
    count = 0
    try:
        for line in f.readlines():
            a, b, c, d = line.rstrip().replace(',','-').split('-')
            # we take the difference of the start and end values of both sets
            left = int(a) - int(c)
            right = int(b) - int(d)
            # if either side is equal we are guaranteed that the other side
            # will form a subset
            if left == 0 or right == 0:
                count += 1
            # otherwise it forms a subset if the sign of the differences differ
            if not copysign(1, left) == copysign(1, right):
                count += 1
    except ValueError:
        pass # end of file
    return count

def part_two(f):
    count = 0
    try:
        for line in f.readlines():
            a, b, c, d = (int(x) for x in line.rstrip().replace(',','-').split('-'))
            if len(range(max(a, c), min(b, d)+1)):
                count += 1
    except ValueError:
        pass # end of file
    return count
