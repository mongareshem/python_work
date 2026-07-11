user_0 = {
    'username': 'shemuz',
    'firstname': 'shem',
    'lastname': "mong'are",
}
for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print()

favorite_languages = {
    'shem': 'python',
    'lawrence': 'javascript',
    'david': 'flutter',
    'sarah': 'c',
}
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print()

for name in favorite_languages.keys():
    print(name.title())

print()

friends = ['shem', 'david']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(f"Hi, {name.title()} I see your favorite language"
              f" is {favorite_languages[name].title()}.")

if 'erin' not in favorite_languages.keys():
    print('\nErin, please take our poll.\n')

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll.')

print()


favorite_languages = {
    'shem': 'python',
    'lawrence': 'javascript',
    'david': 'flutter',
    'sarah': 'python',
    'victoria': 'javascript',
}

for language in favorite_languages.values():
    print(language)

print('\nThe mentioned languages are:')
for language in set(favorite_languages.values()):
    print(language)