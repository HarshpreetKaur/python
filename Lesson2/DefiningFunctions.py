def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
print(cylinder_volume(10, 3))


def print_greeting():
    print('Hello World!')


def population_density(population, land_area):
    return population/land_area

test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))


return_value = print("I wish to register a complaint.")
print(return_value) #None


def print_testcase(expected_value, actual_value):
    print("expected value: {}, actual value: {}".format(expected_value, actual_value))

return_value = print_testcase(42, 42)
print(return_value)

def readable_timedelta(days):
    """Print the number of weeks and days in a number of days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

#OR
def fun(days):
    weeks = int(days/7)
    left = days - 7*weeks
    return str(weeks)+" week(s) and "+str(left)+" day(s)"

print(readable_timedelta(10))
print(fun(10))