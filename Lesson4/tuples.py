def hours2days(input):
    days = int(input/24), input % 24
    return days[0], days[1]