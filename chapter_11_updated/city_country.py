def format_city_country_name(city, country, population=0):
    """A function that returns a neatly formatted city and country name"""
    if population:
        return f'{city.title()}, {country.title()}, population={population}'
    else:
        return f'{city.title()}, {country.title()}'

print(format_city_country_name('nairobi', 'kenya', 7_000_000))