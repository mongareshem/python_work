animals=['cows', 'goats', 'sheep', 'donkeys', 'hens', 'dogs', 'cats']

print(f'The first 3 animals are: {animals[:3]}')
print(f'The middle 3 animals are: {animals[2:5]}')
print(f'The last 3 animals are: {animals[-3:]}\n')

my_pizzas = ['pepperoni', 'cheese', 'vegetarian', 'tomato pie']
friends_pizzas = my_pizzas[:]
print(friends_pizzas)

my_pizzas.insert(4,'Neapolitan')
friends_pizzas.append('Margherita')
print(my_pizzas)
print(friends_pizzas)

print(f'\nMy favorite pizzas are:')
for pizza in my_pizzas:
    print(f'\t\t{pizza}')

print(f"\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(f'\t\t{pizza}')

cakes = ('black forest', 'red velvet', 'chocolate', 'cheese', 'carrot')
print(f'\nOriginal Menu:')
for cake in cakes:
    print(f'\t{cake}')

# cake[2] = 'sponge cake' #Rejected, can't modify a tuple

cakes=('black forest', 'red velvet', 'muffin', 'chocolate', 'ice cream')
print(f'\nRevised Menu:')
for cake in cakes:
    print(f'\t{cake}')