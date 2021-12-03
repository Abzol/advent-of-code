import sys

def ver_one(input):
    numbers = input.readlines()
    total = [0] * len(numbers[0].rstrip())
    for number in numbers:
        for position, digit in enumerate([int(x) for x in number.rstrip()]):
            total[position] += digit
    for i in range(len(total)):
        total[i] = total[i]/(len(numbers)) #ends with newline
    gamma = int("".join([str(int(x > 0.5)) for x in total]), 2)
    epsilon = int("".join([str(int(x <= 0.5)) for x in total]), 2)
    return gamma * epsilon