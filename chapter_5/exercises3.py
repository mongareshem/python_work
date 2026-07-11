usernames = ['admin','shem','stanley','cornelius','john']

if usernames: # We check if the list is empty first then loop afterward
    for username in usernames:
        if username == 'admin':
            print(f'Hello Admin, would you like to see a status report?')
        else:
            print(f'Hello {username.title()}, thank you for logging in again.')
else:
    print('We need to find some users!')

print()

current_users = ['shem', 'john', 'tom', 'king', 'martin']
new_users = ['maal', 'shanice','shem', 'JOHN', 'grace']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'Enter a new username. {new_user.title()} is already in use.')
    elif new_user not in current_users:
        print(f'Username {new_user.title()} is available.')

print()

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')


