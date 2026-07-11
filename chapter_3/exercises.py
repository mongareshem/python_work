friends = ['Asbel', 'Stanley', 'Biqay']

print(f'{friends[0]} is my friend.')
print(f'{friends[1]} is my friend too.')
print(f'{friends[-1]} is my friend as well.')

print(f'\n{friends[0]}, How are ya?')
print(f'{friends[-2]}, You good? ')
print("Hey " + friends[2] + "!\n")

print(f'{len(friends)}\n')

cars = ['gle', 'land cruiser', 'limousine', 'range rover', 'bentley']
print(f'The first car I ever bought was a {cars[0].upper()}.')
print(f'The next car was a {cars[-2].title()}.')
print(f'And now I am on to a {cars[-1].title()}\n')

print(f'{len(cars)}\n')

guests=['Samson', 'Sarah', 'Tabby', 'Raquelle']
print(f'Hey, {guests[0]}, I would like to invite you to dinner!')
print(f'Hey, {guests[1]}, I would like to invite you to dinner!')
print(f'Hey, {guests[2]}, I would like to invite you to dinner!')
print(f'Hey, {guests[3]}, I would like to invite you to dinner!\n')

print(f'Unfortunately, {guests[-3]} cannot make it.')

guests[1] = 'Margaret'
print(guests)
print(f'\nHey, {guests[0]}, I would like to invite you to dinner!')
print(f'Hey, {guests[1]}, I would like to invite you to dinner!')
print(f'Hey, {guests[2]}, I would like to invite you to dinner!')
print(f'Hey, {guests[3]}, I would like to invite you to dinner!\n')

print("I found a bigger dinner table. We can invite more peope")
guests.insert(0,'Benjamin')
guests.insert(3, 'Liz')
guests.append('Violin')
print(guests)

print(f'Hey, {guests[0]}, I would like to invite you to dinner!')
print(f'Hey, {guests[1]}, I would like to invite you to dinner!')
print(f'Hey, {guests[2]}, I would like to invite you to dinner!')
print(f'Hey, {guests[3]}, I would like to invite you to dinner!')
print(f'Hey, {guests[4]}, I would like to invite you to dinner!')
print(f'Hey, {guests[5]}, I would like to invite you to dinner!')
print(f'Hey, {guests[6]}, I would like to invite you to dinner!')

print('\nSadly, only 2 people can be invited for dinner.')
print(f"I'm sorry {guests.pop()}, I am unable to invite you to dinner.")
print(f"I'm sorry {guests.pop()}, I am unable to invite you to dinner.")
print(f"I'm sorry {guests.pop(0)}, I am unable to invite you to dinner.")
print(f"I'm sorry {guests.pop(-2)}, I am unable to invite you to dinner.")
print(f"I'm sorry {guests.pop()}, I am unable to invite you to dinner.\n")
print(guests)

print(f"{guests[0]}, you are invited to dinner.")
print(f"{guests[1]}, you are invited to dinner.")

print(len(guests))

del guests[0]
del guests[0]
print(guests)