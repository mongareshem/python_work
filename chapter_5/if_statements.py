age=19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote?')

age=17
if age >= 18:
    print('\nYou are old enough to vote!')
    print('Have you registered to vote?')
else:
    print('\nSorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18!\n')

age=12
if age<4:
    print('Your admission cost is $0.')
elif age<18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is $10.')

# A better alternative to the if-elif-else block above:
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print(f'Your admission cost is ${price}.')

# Multiple elif blocks
age = 72
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print(f'Your admission cost is ${price}.')

#Omitting the else block
age = 52
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print(f'Your admission cost is ${price}.\n')

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print('Finished making your pizza!')