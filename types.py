print(type(633))
print(type("633"))
print(type(633.0))
print(type("hippo"*12))

count = int(4.0)
print(count)
print(type(count))

house_number = 13
street_name = "The Crescent"
town_name = "Belmont"
print(type(house_number))
address = str(house_number) + " " + street_name + ", " + town_name
print(address)

grams_of_sugar = float("35.0")
print(grams_of_sugar)
print(type(grams_of_sugar))


mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
total = int(mon_sales)+int(tues_sales)+int(wed_sales)+int(thurs_sales)+int(fri_sales)
print("This week's total sales: " + str(total))