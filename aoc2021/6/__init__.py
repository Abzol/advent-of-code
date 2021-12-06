import sys

#bad
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

#fasty as fuck
def simulate_many_fish(seed, days):
    fish = [0,0,0,0,0,0,0,0,0]
    for x in seed:
        fish[x] += 1
    for day in range(days):
        spawn = fish.pop(0)
        fish.append(spawn)
        fish[6] += spawn
    return sum(fish)

def ver_one(input):
    fish = [int(x) for x in input.read().split(',')]
    return simulate_many_fish(fish, 80)

def ver_two(input):
    fish = [int(x) for x in input.read().split(',')]
    return simulate_many_fish(fish, 256)