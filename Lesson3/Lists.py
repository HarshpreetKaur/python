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