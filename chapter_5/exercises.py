car = 'mercedes'
print("I predict that car=='mercedes' evaluates to True")
print(car == 'mercedes')

print("I predict that car=='toyota' evaluates to False")
print(car =='toyota')

topping = 'cheese'
print("\nI predict that topping == 'cheese' evaluates to True")
print(topping == 'cheese')

print("I predict that topping = 'pepperoni' evaluates to False")
print(car =='pepperoni')

bike = 'honda'
print("\nI predict that bike == 'honda' evaluates to True")
print(bike == 'honda')

print("I predict that bike == 'Honda' evaluates to False")
print(bike =='Honda')

username = 'Shem Samson'
if username == 'Shem Samson':
    print("\nUser found!")

username = "Shem Mong'are"
if username != 'Shem Samson':
    print("User not found!")

username = "Shem Mong'are"
if username.lower() == "shem mong'are":
    print("User found!")

print()

age = 13
if age < 18:
    print("You are a minor.")

if age == 18:
    print('You are just an adult.')

if age >= 18:
    print("You are old enough.")

print()

value1 = 10
value2 = 20

print(value1 <= 10 and value2 <= 20)
print(value1 >= 5 and value2 >= 15)
print(value1 >= 23 and value2 <= 15)
print(value1 > 3 and value2 < 25)

print()

print(value1 >= 23 or value2 <= 15)
print(value1 <= 23 or value2 <= 15)
print(value1 >= 23 or value2 >= 15)

toppings = ['cheese', 'pepperoni', 'olives', 'avocado', 'anchovies']
print(f'\n{'cheese' in toppings}')
print(f'{'pineapple' in toppings}')