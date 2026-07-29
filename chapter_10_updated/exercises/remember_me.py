from pathlib import Path
import json

print("Press 'q' to quit.")
path = Path('remember_me.json')
user_details = {}

while True:
    username = input('\nWhat is your name? ')
    if username.lower() == 'q':
        break

    unique_numbers = []
    birthday = input('What is your birthday? ')
    if birthday.lower() == 'q':
        break
    else:
        unique_numbers.append(birthday)

    reg_number = input('What is your reg number? ')
    if reg_number.lower() == 'q':
        break
    else:
        unique_numbers.append(reg_number)

    if f'{username}' not in user_details.keys():
        user_details[f'{username}'] = unique_numbers
        user_dict = json.dumps(user_details)
        path.write_text(user_dict)
    else:
        print(f'The username {username} already exists!')
        continue
