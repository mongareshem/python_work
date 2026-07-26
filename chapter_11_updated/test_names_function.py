from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Shem Samson' work?"""
    formatted_name = get_formatted_name('shem', 'samson')
    assert formatted_name == 'Shem Samson'