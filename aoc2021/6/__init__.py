import sys

def simulate_fish(seed, days):
    fish = seed
    for day in range(days):
        new_fish = []
        for timer in fish:
            if timer > 0:
                new_fish.append(timer-1)
            else:
                new_fish.append(6)
                new_fish.append(8)
    return len(fish)

def ver_one(input):
    fish = [int(x) for x in input.read().split(',')]
    return simulate_fish(fish, 80)

def ver_two(input):
    fish = [int(x) for x in input.read().split(',')]
    return None #slow as hell