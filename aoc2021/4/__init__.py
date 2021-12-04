import sys

def ver_one(input):
    data = input.read().split('\n\n')
    numbers = [int(x) for x in data[0].split(',')]
    boards = [x.split() for x in data[1:]]
    for i, board in enumerate(boards):
        boards[i] = [int(x) for x in board]

    called_numbers = []

    for number in numbers:
        called_numbers.append(number)
        for i, board in enumerate(boards):
            for j in range(5):
                if (all([x in called_numbers for x in board[j*5:(j*5)+5]])) or (all([x in called_numbers for x in board[j::5]])):
                    return sum([x for x in board if x not in called_numbers])*called_numbers[-1]

def ver_two(input):
    data = input.read().split('\n\n')
    numbers = [int(x) for x in data[0].split(',')]
    boards = [x.split() for x in data[1:]]
    for i, board in enumerate(boards):
        boards[i] = [int(x) for x in board]

    def loop_through():
        called_numbers = []
        for number in numbers:
            called_numbers.append(number)
            for i, board in enumerate(boards):
                for j in range(5):
                    if (all([x in called_numbers for x in board[j*5:(j*5)+5]])) or (all([x in called_numbers for x in board[j::5]])):
                        if len(boards) == 1:
                            return sum([x for x in board if x not in called_numbers])*called_numbers[-1]
                        else:
                            del boards[i]
                            return
    x = loop_through()
    while x == None:
        x = loop_through()
    return x