def city_country(city = 'Santiago', country = 'Chile'):
    return city.title() + ', ' + country.title()

print (city_country('novogrudok', 'belarus'))
print (city_country('minsk', 'belarus'))
print (city_country())