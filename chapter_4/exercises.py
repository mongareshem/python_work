pizzas = ['pepperoni', 'cheese', 'vegetarian', 'tomato pie']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print('I really like pizza!\n')

animals=['cows', 'goats', 'sheep']
for animal in animals:
    print(f'{animal.title()} would make great domestic animals.')
print("Any of these animals could be very productive.\n")

for number in range(1,21):
    print(f'{number}')

# million=[]
# for number in range(1, 1000001):
#     million.append(number)
# print(million)
# print(f'\nMax: {max(million)}')
# print(f'Min: {min(million)}')
# print(f'Sum: {sum(million)}\n') #Formula: S={n(n+1)}/2

odd_numbers=[]
for odd_number in range(1,21,2):
    odd_numbers.append(odd_number)
print(f'\n{odd_numbers}')

odd_numbers = list(range(1,21,2)) #An alternative
print(odd_numbers)

odd_numbers=[value for value in range(1,21,2)] #An alternative
print(odd_numbers)

print(f'{[value for value in range(1, 21, 2)]}\n') #A better alternative

threes = []
for three in range(3,30,3):
    threes.append(three)
print(threes)

print(list(range(3,30,3))) # A better alternative to the for loop above

cubes=[]
for value in range(1,11):
    cubes.append(value**3)
print(f'\nCubes: {cubes}')

cubes=[value**3 for value in range(1,11)]
print(f'Cubes: {cubes}')

print(f'Cubes: {[value**3 for value in range(1,11)]}') #Better alternative