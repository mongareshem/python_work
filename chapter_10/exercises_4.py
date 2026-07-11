import json

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
        check_username = input(f"Is {user} the correct username? (y/n): ")
        if check_username == 'y':
            print(f"Welcome back, {user}!")
        else:
            user = get_new_username()
            print(f"We'll remember you when you come back {user}!")
    else:
        user = get_new_username()
        print(f"We'll remember you when you come back {user}!")


greet_user()