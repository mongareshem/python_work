person = {
    'firstname': 'Samson',
    'lastname': 'Momanyi',
    'age': 60,
    'city': 'Nairobi',
}
print(person['firstname'])
print(person['lastname'])
print(person['age'])
print(person['city'])

print()

favorite_numbers = {
    'shem': 1,
    'antony': 110,
    'clinton': 2,
    'brian': 76,
    'bruce': 7,
}
for name,number in favorite_numbers.items():
    print(f"{name.title()}: {number}")

print()

glossary = {
    'print': 'used to display information on the terminal',
    'append': 'used to add items to the end of a string',
    'del': 'used to permanently delete items from lists and dictionaries',
    'set': 'a list that has unique items only',
    'sorted': 'a function that temporarily organizes stuff in alphabetical order',
    'capitalize': 'a method that capitalizes the first letter in the first word.',
    'strip': 'removes whitespaces from characters - rstrip/lstrip',
    'tuple': 'an immutable list',
    'not in': 'used to confirm that characters are missing',
    'callable(C)': 'includes functions such as range() and len()',
    'pointers(P)': 'a variable that stores the memory address of another variable',
    'pointers': 'python uses object references rather than raw pointers',
    'debugging': 'the process of finding and fixing errors.',
    'breakpoint': 'a marker set in code at a specific line to pause program execution for debugging.',
}
for word,definition in glossary.items():
    print(f"{word.title()}: \n\t{definition.capitalize()}.")

print()

rivers = {
    'nile': 'egypt',
    'tana': 'kenya',
    'amazon': 'brazil',
}
for river,country in rivers.items():
    print(f"The River {river.title()} runs through {country.capitalize()}.")

print()

favorite_languages = {
    'shem': 'python',
    'lawrence': 'javascript',
    'david': 'flutter',
    'sarah': 'c',
}
poll_participants = ['shem', 'maal', 'favor', 'david', 'elsy', 'lawrence', 'sarah']

for poll_participant in poll_participants:
    if poll_participant in favorite_languages.keys():
        print(f'{poll_participant.title()}, thank you for taking the poll.')
    else:
        print(f'{poll_participant.title()}, you are invited to take the poll.')
