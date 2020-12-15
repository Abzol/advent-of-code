def ver_one(input):
    answers = set()
    total = 0
    for line in input.readlines():
        line = line.rstrip()
        if line != '':
            for c in list(line):
                answers.add(c)
        else:
            total += len(answers)
            answers = set()
    total += len(answers)
    return total

def ver_two(input):
    answers = set()
    total = 0
    group = []
    for line in input.readlines():
        line = line.rstrip()
        if line != '':
            person = set()
            for c in list(line):
                person.add(c)
            group.append(person)
        else:
            answers = group[0]
            for member in group[1:]:
                answers &= member
            total += len(answers)
            answers = set()
            group = []
    answers = group[0]
    answers &= group[1]
    total += len(answers)
    return total