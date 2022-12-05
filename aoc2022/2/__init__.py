values = {
    'rock' : 1,
    'paper' : 2,
    'scissors' :3,
    'win' : 6,
    'draw' : 3,
    'lose' : 0
}

outcomes = {
    'A' : {
        'X' : values['rock'] + values['draw'],
        'Y' : values['paper'] + values['win'],
        'Z' : values['scissors'] + values['lose']
    },
    'B' : {
        'X' : values['rock'] + values['lose'],
        'Y' : values['paper'] + values['draw'],
        'Z' : values['scissors'] + values['win']
    },
    'C' : {
        'X' : values['rock'] + values['win'],
        'Y' : values['paper'] + values['lose'],
        'Z' : values['scissors'] + values['draw']
    }
}

def part_one(f):
    score = 0
    try:
        for line in f.readlines():
            opponent, you = line.split()
            score += outcomes[opponent][you]
    except ValueError:
        pass # end of list
    return score

def part_two(f):
    key = {
        'A' : 'rock',
        'B' : 'paper',
        'C' : 'scissors',
        'X' : 'lose',
        'Y' : 'draw',
        'Z' : 'win'
    }
    score = 0
    try:
        for line in f.readlines():
            opponent, outcome = line.split()
            if outcome == 'Y':
                you = opponent
            if outcome == 'X':
                you = 'ABC'['ABC'.index(opponent) -1]
            if outcome == 'Z':
                you = 'ABCA'['ABC'.index(opponent) +1]
            score += values[key[outcome]] + values[key[you]]
    except ValueError:
        pass # end of list
    return score
