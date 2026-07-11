alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print()

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("....")

print(f'The total number of aliens created is {len(aliens)}.')

print()

# Dictionaries in a list OR a list of dictionaries
aliens = [] #List
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} #dictionary
    aliens.append(new_alien)

for alien in aliens[:3]: #for each dictionary(alien) in the list(aliens)
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)

print()

# Lists in a dictionary OR a dictionary of lists
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(f'You ordered a {pizza["crust"]}-crust pizza with the following toppings:')

for topping in pizza['toppings']:
    print(f'\t{topping}')

print()
print(pizza['toppings'][1].title()) # Other methods can be tried out as well

favorite_languages = {
    'shem': ['python', 'javascript'],
    'lawrence': ['javascript', 'node.js'],
    'david': ['flutter',],
    'sarah': ['c', 'java'],
}
for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")

    for language in languages:
        print(language.title())

print()

favorite_languages = {
    'shem': ['python', 'javascript'],
    'lawrence': ['javascript', 'node.js'],
    'david': ['flutter',],
    'sarah': ['c', 'java'],
}
for name,languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(language.title())
    else:
        print(f"\n{name.title()}'s favorite language is: {languages[0].title()}")

print()

users = {
    'shem': {
        'firstname': 'shem',
        'lastname': "mong'are",
        'location': 'nairobi'
    },
    'victoria': {
        'firstname': 'victoria',
        'lastname': 'lucy',
        'location': 'kiambu',
    },
}

for username, info in users.items():
    print(f'\nUsername: {username}')
    print(f'\tFullname: {info["firstname"].title()} {info["lastname"].title()}')
    print(f"\tLocation: {info['location'].title()}")