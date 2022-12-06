def load_stacks(f):
    stacks = {}
    # diagram
    line = f.readline()
    for i in range((len(line)//4)):
        stacks[i+1] = []
    while not line.startswith('\n'):
        for i, box in enumerate(line[1::4], start=1):
            if box != ' ':
                stacks[i].append(box)
        line = f.readline()
    for stack in stacks:
        stacks[stack] = stacks[stack][::-1] # reverse
        stacks[stack] = stacks[stack][1:] # pop front
    return stacks

def part_one(f):
    stacks = load_stacks(f)

    # move ops
    for line in f.readlines():
        if not line.startswith('\n'):
            num, src, dst = (int(x) for x in line.split()[1::2])
            for _ in range(num):
                stacks[dst].append(stacks[src].pop())
        else: # end of file
            return ''.join([stacks[x][-1] for x in stacks])

def part_two(f):
    stacks = load_stacks(f)

    for line in f.readlines():
        if not line.startswith('\n'):
            num, src, dst = (int(x) for x in line.split()[1::2])
            stacks[dst].extend(stacks[src][-num:])
            stacks[src] = stacks[src][:-num+len(stacks[src])]
        else: # end of file
            return ''.join([stacks[x][-1] for x in stacks])
