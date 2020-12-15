def generate_rules(input):
    rules = {}
    for line in input.readlines():
        rule = [x.strip() for x in line.split('contain')]
        bag = " ".join(rule[0].split()[:-1])
        contains = [x.strip() for x in rule[1].split(',')]
        contains[-1] = contains[-1].replace('.', '') #get rid of a trailing period
        contents = {}
        for contain in contains:
            if contain != 'no other bags':
                number, bags = contain.split(' ',1)
                contents[" ".join(bags.split()[:-1])] = number
            else:
                contents = None
        rules[bag] = contents
    return rules

def can_contain(rules, kind, target):
    try:
        if target in list(rules[kind].keys()):
            return True
        else:
            inner = False
            for content in list(rules[kind].keys()):
                if can_contain(rules, content, target):
                    inner = True
            return inner
    except AttributeError:
        return False

def count_contains(rules, kind):
    total = 0
    contents = rules[kind]
    if contents == None:
        return 1
    else:
        for bag in contents:
            total += int(rules[kind][bag]) * count_contains(rules, bag)
    return total+1

def ver_one(input):
    rules = generate_rules(input)
    total = 0
    for kind in rules:
        if (can_contain(rules, kind, 'shiny gold')):
            total += 1
    return total

def ver_two(input):
    rules = generate_rules(input)
    return count_contains(rules, 'shiny gold')-1