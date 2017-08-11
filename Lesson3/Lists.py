def how_many_days(month_number):
   
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    return days_in_month[month_number-1]

print(how_many_days(8))


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
q3 = months[6:9]
print(q3)
first_half = months[:6]
print(first_half)
second_half = months[6:]
print(second_half)


eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# it prints the last three elements of the list
print(eclipse_dates[-3:])


dish = ["Spam", "Spam", "Spam", "Spam", "Spam", "Spam", "baked beans", "Spam", "Spam", "Spam", "Spam"]
mr_buns_order = dish
print(dish)
print(mr_buns_order)
dish[6] = "Spam" #baked beans are off
print(mr_buns_order)
print(dish)


batch_sizes = [15, 6, 89, 34, 65, 35]
print(max(batch_sizes))

print(sorted(batch_sizes))
print(sorted(batch_sizes, reverse=True))

nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)

names = ["García", "O'Kelly", "Davis"]
print("-".join(names))


def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    return (sorted(input_list, reverse=True)[:3])


def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    middle_index = int(len(numbers)/2)
    if(len(numbers)%2 == 0):
        median = (numbers[middle_index]+numbers[middle_index-1])/2
    else:
        median = numbers[middle_index]
    return median

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))

