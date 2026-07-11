cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
print(f"\n{car=='bmw'}")
print(car=='audi')
print(car=='Bmw')
print(car.upper()=='BMW')

car2 = 'Audi'
print(car2.lower()=='audi')
name = 'John'
print(f"{name.lower() == 'john'}\n")

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

age=18
print(age==18)

answer=17
if answer != 7:
    print('\nThat is not the correct answer. Please try again!\n')

age_0=22
age_1=18

#AND
print((age_0 >= 21) and (age_1 >= 21)) #Parentheses are for readability
age_1=23
print(age_0>=21 and age_1>=21)

#OR
print(f'\n{age_0 >= 22 or age_1 >= 22}')
age_1 =16
print(age_0>=22 or age_1>=22)
print(age_0>=25 or age_1>=25)

requested_toppings =['mushrooms', 'onions', 'pineapple']
print(f"\n{'mushrooms' in requested_toppings}")
print('pepperoni' in requested_toppings)

banned_users =['andrew', 'carolina', 'david']
users='marie'

if users not in banned_users:
    print(f"\n{users.title()}, you can post a comment if you wish.\n")

game_active=True
can_edit=False

print(game_active)
print(can_edit)