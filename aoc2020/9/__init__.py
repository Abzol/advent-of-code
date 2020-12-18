def validate(number, options):
    possibilities = set()
    for i in options:
        for j in options:
            if (i != j):
                possibilities.add(i+j)
    return number in possibilities

def find_invalid(numbers):
    for index, line in enumerate(numbers):
        if index >= 25:
            if validate(line, numbers[index-25:index]) == False:
                return line

def scan_invalid(target, numbers):
    total = 0
    for index, number in enumerate(numbers):
        total += number
        if total > target:
            return False
        if total == target:
            return index

def ver_one(input):
    return find_invalid([int(x) for x in input.readlines()])

def ver_two(input):
    numbers = [int(x) for x in input.readlines()]
    invalid = find_invalid(numbers)
    for i in range(len(numbers)):
        j = scan_invalid(invalid, numbers[i:])
        if j:
            return min(numbers[i:i+j]) + max(numbers[i:i+j])