def list_seats(data):
    seats = set()
    for line in data.readlines():
        trans = "".maketrans('FBLR', '0101')
        seat = line.translate(trans)
        seat = int(seat, 2)
        seats.add(seat)
    return seats

def ver_one(input):
    return max(list_seats(input))

def ver_two(input):
    seats = list_seats(input)
    missing_seats = set(range(1024)) - seats
    for seat in missing_seats:
        if seat-1 in seats and seat+1 in seats:
            return(seat)