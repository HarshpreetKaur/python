phone_balance = 5
bank_balance = 300
if phone_balance < 10:
   phone_balance += 10
   bank_balance -= 10
print(phone_balance)
print(bank_balance)

weight_in_kg = 60
height_in_m = 1.69164
if 18.5 <= weight_in_kg / (height_in_m)**2 < 25:
	print("BMI is considered 'normal'.")

number = 5567876543
if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")


def garden_calendar(season):
    if season == "spring":
        print("time to plant the garden!")
    elif season == "summer":
        print("time to water the garden!")
    elif season == "autumn" or season == "fall":
        print("time to harvest the garden!")
    elif season == "winter":
        print("time to stay indoors and drink tea!")
    else:
        print("I don't recognize that season")

garden_calendar("spring")


def which_prize(points):
    """
    Returns the prize
    """
    if points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif points <= 150:
        return "Oh dear, no prize this time."
    elif points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"

print(which_prize(123))


is_raining = True
is_sunny = False
if is_raining and is_sunny:
    print("Is there a rainbow?")


def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return top_area + side_area
    else:
        return side_area

print(cylinder_surface_area(10, 20, True))


errors = 3
if errors:
    print("There are " + str(errors) + " mistakes. Please correct.")
else:
    print("No mistakes here!")


def which_prize2(points):
    
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 150 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."