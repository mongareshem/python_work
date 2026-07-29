from pathlib import Path
import json

print("Press 'q' to quit.")
path = Path('remember_me.json')
user_details = {}

while True:
    username = input('What is your name? ')
    if username.lower() == 'q':
        break

    birthday = input('What is your birthday? ')
    if birthday.lower() == 'q':
        break

    user_details[f'{username}'] = birthday
    user_dict = json.dumps(user_details)
    path.write_text(user_dict)


