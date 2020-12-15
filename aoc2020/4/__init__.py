def digest_passport(data):
    passport = {}
    fields = data.split()
    for field in fields:
        key, value = field.split(':')
        passport[key] = value
    return passport

def validate_passport(passport):
    if all([x in passport for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]):
        return True

def certify_passport(passport):
    try:
        byr = int(passport['byr'])
        if (len(str(byr)) != 4 or byr < 1920 or byr > 2002):
            return False
        iyr = int(passport['iyr'])
        if (len(str(byr)) != 4 or iyr < 2010 or iyr > 2020):
            return False
        eyr = int(passport['eyr'])
        if (len(str(eyr)) != 4 or eyr < 2020 or eyr > 2030):
            return False
        unit = passport['hgt'][-2:]
        try:
            hgt = int(passport['hgt'][:-2])
        except ValueError:
            return False
        if unit == 'cm':
            if hgt < 150 or hgt > 193:
                return False
        elif unit == 'in':
            if hgt < 59 or hgt > 76:
                return False
        else:
            return False
        hcl = passport['hcl']
        if hcl[0] != '#' or all([x in hcl[1:] for x in list("abcdef0123456789")]):
            return False
        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        if len(passport['pid']) != 9:
            return False
    except KeyError:
        return False
    return True

def ver_one(input):
    total = 0
    data = ""
    for line in input.readlines():
        if line.rstrip() != '':
            data += (" " + line)
        else:
            if validate_passport(digest_passport(data)):
                total += 1
            data = ""
    if validate_passport(digest_passport(data)):
        total += 1
    return total


def ver_two(input):
    total = 0
    data = ""
    for line in input.readlines():
        if line.rstrip() != '':
            data += (" " + line)
        else:
            if certify_passport(digest_passport(data)):
                total += 1
            data = ""
    if certify_passport(digest_passport(data)):
        total += 1
    return total