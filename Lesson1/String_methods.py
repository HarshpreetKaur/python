print("charlotte hippopotamus turner".title())

full_name = "charlotte hippopotamus turner"
print(full_name.islower())

print("One fish, two fish, red fish, blue fish.".count('fish'))

prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"
vowel_count = 0
vowel_count = prophecy.count("a") + prophecy.count("e") + prophecy.count("i") + prophecy.count("o") + prophecy.count("u") + prophecy.count("A") + prophecy.count("E") + prophecy.count("I") + prophecy.count("O") + prophecy.count("U")
print(vowel_count)

#OR
vowel_count += prophecy.count('a')
vowel_count += prophecy.count('A')
vowel_count += prophecy.count('e')
vowel_count += prophecy.count('E')
vowel_count += prophecy.count('i')
vowel_count += prophecy.count('I')
vowel_count += prophecy.count('o')
vowel_count += prophecy.count('O')
vowel_count += prophecy.count('u')
vowel_count += prophecy.count('U')

#OR
vowel_count = 0
lower_prophecy = prophecy.lower()
vowel_count += lower_prophecy.count('a')
vowel_count += lower_prophecy.count('e')
vowel_count += lower_prophecy.count('i')
vowel_count += lower_prophecy.count('o')
vowel_count += lower_prophecy.count('u')

user_ip = "208.94.117.90"
url = "/bears/koala"
now = "16:20"
log_message = "IP address {} accessed {} at {}".format(user_ip, url, now)

city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"
#alert = "Today's forecast for " + city + ": The temperature will range from " + str(low_temperature) + " to " + str(high_temperature) + " " + temperature_unit + ". Conditions will be " + weather_conditions + "."
alert = "Today's forecast for {0}: The temperature will range from {1} to {2} {3}. Conditions will be {4}.".format(city, str(low_temperature), str(high_temperature), temperature_unit, weather_conditions)
print(alert)