from city_country import format_city_country_name

def test_city_country():
    """Do arguments like 'Santiago, Chile' work?"""
    formatted_name = format_city_country_name('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'


def test_city_country_population():
    formatted_name = format_city_country_name('santiago', 'chile',
                                              5_000_000)
    assert formatted_name == 'Santiago, Chile, population=5000000'