import sys

def ver_one(input):
    crabs = [int(x) for x in input.read().split(',')]
    best_position = None
    best_cost = None
    for position in range(min(crabs), max(crabs)):
        fuel_cost = sum([abs(position - crab) for crab in crabs])
        if best_cost == None or fuel_cost < best_cost:
            best_cost = fuel_cost
    return best_cost

def ver_two(input):
    crabs = [int(x) for x in input.read().split(',')]
    best_position = None
    best_cost = None
    for position in range(min(crabs), max(crabs)):
        fuel_cost = sum([sum(list(range(1,abs(position - crab)+1))) for crab in crabs])
        if best_cost == None or fuel_cost < best_cost:
            best_cost = fuel_cost
        doneness = int(position/(max(crabs)-(min(crabs)))*100)
        print(f'...{doneness}% done', end='\r')
    print('            ', end='\r') #clean up 
    return best_cost