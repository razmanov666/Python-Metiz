from task11_1_function import *

print("Enter 'q' at any time for quit.")
while True:
    city = input('Enter city:\n')
    if city == 'q':
        break
    country = input('Enter city:\n')
    if country == 'q':
        break
    population = input('Enter population:\n')
    if population == 'q':
        break
    formatted_place = get_formatted_city_country(city, country, population)
    print("\nNeatly formatted name: " + formatted_name)