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

def ver_two(input):
    numbers = input.readlines()
    oxy_rates = numbers.copy()
    co2_rates = numbers.copy()
    for i in range(len(numbers[0])-1):
        popular = int((sum([int(x[i]) for x in oxy_rates]) >= (len(oxy_rates)/2)))
        new_oxy_rates = []
        new_co2_rates = []
        if len(oxy_rates) > 1:
            for number in oxy_rates:
                if int(number[i]) == popular:
                    new_oxy_rates.append(number)
            oxy_rates = new_oxy_rates
        popular = int((sum([int(x[i]) for x in co2_rates]) >= (len(co2_rates)/2)))
        if len(co2_rates) > 1:
            for number in co2_rates:
                if int(number[i]) != popular:
                    new_co2_rates.append(number)
            co2_rates = new_co2_rates
    return int(oxy_rates[0].rstrip(), 2) * int(co2_rates[0].rstrip(), 2)