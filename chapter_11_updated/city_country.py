def format_city_country_name(city, country):
    """A function that returns a neatly formatted city and country name"""
    return f'{city.title()}, {country.title()}'

print(format_city_country_name('nairobi', 'kenya'))