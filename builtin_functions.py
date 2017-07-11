length = len("Python")
print(length)

given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"

name_length = len(given_name + " " + middle_names + " " + family_name)
# or name_length = len(given_name + middle_names + family_name) + 2

driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)