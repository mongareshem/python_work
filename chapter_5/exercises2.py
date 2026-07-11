alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points!')
else:
    print("You just earned 10 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print('You just earned 10 points')

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')

print()

age = 38
if age < 2:
    print('You are a baby.')
elif age < 4:
    print('You are a toddler.')
elif age < 13:
    print('You are a kid.')
elif age < 20:
    print('You are a teenager.')
elif age < 65:
    print('You are an adult.')
else:
    print('You are an elder')

print()

favorite_fruits = ['avocado','mangoes','pineapples']
if 'avocado' in favorite_fruits:
    print("You really like avocados!")
if 'mangoes' in favorite_fruits:
    print('You really like mangoes!')
if 'pineapples' in favorite_fruits:
    print("You really like pineapples!")
if 'bananas' not in favorite_fruits:
    print('You do not like bananas that much')
if 'watermelons' not in favorite_fruits:
    print('You do not like watermelons that much as well.')