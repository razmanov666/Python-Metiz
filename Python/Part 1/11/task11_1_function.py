def get_formatted_city_country(city, country, population=''):
    """Возвращает отформатированные город и страну."""
    if population:
        formatted_place = (city + ', ' + country 
                            + ' – ' + str(population) + '.')
    else:
        formatted_place = (city + ', ' + country + '.')
    return (formatted_place.title())