unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print()

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')
    # print(pets) # To see how the list removes 'cat' stepwise
print(pets)

print()

responses = {}
poll_active = True

while poll_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let someone else to respond? (yes/no): ")
    if repeat == 'no':
        poll_active = False

print('\n----Poll Results----')
for name, response in responses.items():
    print(f'{name.title()} would like to climb {response.title()}.')