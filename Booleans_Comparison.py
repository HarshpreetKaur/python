the_sun_is_up = True
the_sky_is_blue = False
print(1 < 2)
print(42 > 43)


sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)