import json

username = input('What is your name? ')

filename = 'username.json'

# Saving user-generated data
with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print(f"We'll remember you when you come back {username}!")

# Reading user-generated data
with open(filename) as file_object:
    username = json.load(file_object)
print(f"Welcome back {username}!")

print("----------------------------------------------------------\n")


# Using a TRY-EXCEPT to combine the json.dump(data, f_obj) and json.load(f_obj)
# filename = 'user.json'
# try:
#     with open(filename, 'r') as f_object:
#         user = json.load(f_object)
# except FileNotFoundError:
#     user = input("What is your name? ")
#     with open(filename, 'w') as f_object:
#         json.dump(user, f_object)
#         print(f"We'll remember you when you come back {user}!")
# else:
#     print(f'Welcome back, {user}!')


# REFACTORING
def get_stored_username():
    """Get stored username if available."""
    file = 'user.json'
    try:
        with open(file, 'r') as f_object:
            user = json.load(f_object)
    except FileNotFoundError:
        return None
    else:
        return user


def get_new_username():
    """Prompt for a new username"""
    user = input("What is your name? ")
    file = 'user.json'
    with open(file, 'w') as f_object:
        json.dump(user, f_object)
    return user


def greet_user():
    """Greet the user by name."""
    user = get_stored_username()
    if user:
        print(f"Welcome back, {user}!")
    else:
        user = get_new_username()
        print(f"We'll remember you when you come back {user}!")
        
greet_user()