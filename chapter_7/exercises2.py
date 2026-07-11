sandwich_orders = ['burrito', 'Reuben', 'melt', 'panini', 'pastrami', 'tuna']
finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order} sandwich.")
    finished_sandwiches.append(sandwich_order)

print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(f'\t{finished_sandwich.title()}')

print("----------------------------------------------------")

sandwich_orders = ['burrito', 'pastrami', 'pastrami', 'panini', 'pastrami', 'tuna']
finished_sandwiches = []

print("Deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order} sandwich.")
    finished_sandwiches.append(sandwich_order)

print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(f'\t{finished_sandwich.title()}')

print("-------------------------------------------------")

dream_places = {}
poll = True
while poll:
    user = input("What is your name? ")

    if user == 'quit':
        poll = False
    else:
        place = input('If you could visit one place in the world, where would you go? ')
        dream_places[user] = place

print("\n-***************************************-")
for user, place in dream_places.items():
    print(f"{user.title()}: {place.title()}")