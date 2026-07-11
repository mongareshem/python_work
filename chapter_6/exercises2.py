person_1 = {
    'firstname': 'Samson',
    'lastname': 'Momanyi',
    'age': 60,
    'city': 'Nairobi',
}
person_2 = {
    'firstname': 'Enoch',
    'lastname': 'Subano',
    'age': 26,
    'city': 'Nyamira',
}
person_3 = {
    'firstname': 'Margaret',
    'lastname': 'Onyancha',
    'age': 45,
    'city': 'Kisii',
}
persons = [person_1, person_2, person_3]
for person in persons:
    print(f"\nName: {person['firstname']} {person['lastname']} ")
    print(f"Age: {person['age']}, City: {person['city']}")

print()

tom = {'type': 'cat', 'owner': 'Leah',}
bosco = {'type': 'dog', 'owner': 'mambo'}
luck = {'type': 'bird', 'owner': 'Tusk'}

pets = [tom, bosco, luck]

for pet in pets:
    print(f"Type: {pet['type']}, Owner: {pet['owner'].title()}")

print()

favorite_places = {
    'shem': ['maldives', 'USA', 'manchester','Diani, Summer tides', 'china'],
    'val': ['maldives', 'nairobi', 'kisumu'],
    'steve': ['madrid', 'london']
}
for name,places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

print()

favorite_numbers = {
    'shem': [1, 5, 2, 3, 7, 10],
    'antony': [110, 72, 45],
    'clinton': [2, 1, 4],
    'brian': [76, 34, 1],
    'bruce': [7, 5, 8, 10],
}
for name,numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: {numbers}")

print()

cities = {
    'nairobi': {
        'country': 'kenya',
        'population': '8M',
        'fact': 'a business hub.'
    },
    'male': {
        'country': 'maldives',
        'population': '10M',
        'fact': 'a recreational city, fit for vacations.'
    },
    'beijing': {
        'country': 'china',
        'population': '56M',
        'fact': 'a scientific-fast city.'
    }
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"{info['country'].title()}, {info['population']} people")
    print(f"{info['fact'].capitalize()}")