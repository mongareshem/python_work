from city_country import format_city_country_name

def test_city_country():
    """Do arguments like 'Santiago, Chile' work?"""
    formatted_name = format_city_country_name('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'