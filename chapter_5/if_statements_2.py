requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if 'green peppers' in requested_topping:
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f'Adding {requested_topping}.')

print(f'Finished making your pizza!\n')

requested_toppings = []
if requested_toppings: #If a list is empty, evaluates to false, doesn't run.
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print(f'Finished making your pizza!')
else:
    print('Are you sure you want a plain pizza?\n')

# Working with multiple lists
available_toppings = ['mushrooms', 'green peppers', 'extra cheese',
                      'olives', 'pineapple', 'pepperoni']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping} here.")
print('Finished making your pizza!')

