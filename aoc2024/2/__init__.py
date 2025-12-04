def part_one(puzzle):
    reports = []
    for line in puzzle.readlines():
        reports.append([int(x) for x in line.split()])
    safe = 0
    for levels in reports:
        adj = zip(levels, levels[1:])
        if (  all(i < j for i,j in adj) # strict increment
           or all(i > j for i,j in adj)): # strict decrement
            if (  any(abs(i-j) > 3 for i,j in adj)
               or any(i == j for i,j in adj)):
                continue
            else:
                safe +=1
    return safe
