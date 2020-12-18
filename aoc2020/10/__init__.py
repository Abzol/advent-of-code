def ver_one(input):
    numbers = sorted([int(x) for x in input.readlines()])
    numbers.insert(0, 0) #add charging port
    ones = 0
    threes = 1 #add device
    for index, value in enumerate(numbers):
        try:
            if numbers[index+1] - value == 1:
                ones += 1
            if numbers[index+1] - value == 3:
                threes += 1
        except IndexError:
            pass
    return ones * threes

def ver_two(input):
    numbers = sorted([int(x) for x in input.readlines()])
    numbers.insert(0, 0) #add charging port
    numbers.append(numbers[-1]+3) #add device
    graph = {}
    for index, value in enumerate(numbers[::-1]):
        paths = 0
        for i in range(3):
            compared = numbers[-(index-i)]
            if compared > value:
                if compared - value <= 3:
                    try:
                        paths += graph[compared] or 1
                    except KeyError:
                        paths += 1
        graph[value] = paths
    return graph[0]