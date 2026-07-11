def greet_user():
    """Display a simple greeting""" #A docstring (more or less a comment)
    print("Hello!")

greet_user()
greet_user()

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello {username.title()}!")

greet_user("shem")
greet_user('sarah')

print()

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("cat", "tom")
describe_pet("dog", 'bosco')
describe_pet("tom", "cat") #ORDER MATTERS in positional arguments

# Keyword Arguments
describe_pet(animal_type="cat", pet_name="willie")
describe_pet(pet_name="bosco", animal_type="dog") #ORDER DOESN'T MATTER, name-value does

print()

def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="tommy") #no need for animal_type
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="harry")
describe_pet("willie")
# describe_pet() #TypeError: Arguments given are fewer than expected
# describe_pet("tom", "jerry", "cats") #TypeError: excess arguments

print()

def get_formatted_name (firstname, lastname):
    """Return a full name, neatly formatted."""
    fullname = f"{firstname} {lastname}"
    return fullname.title()

programmer = get_formatted_name("shem" ,"mong'are")
print(programmer)

print()

def get_formatted_name (firstname, lastname, middlename = ''):
    """Return a full name, neatly formatted."""
    if middlename:
        fullname = f"{firstname} {middlename} {lastname}"
    else:
        fullname = f"{firstname} {lastname}"
    return fullname.title()

programmer = get_formatted_name("shem" ,"mong'are")
print(programmer)

developer = get_formatted_name("shem", "samson", "mong'are")
print(developer)

print()

def build_person(firstname, lastname):
    """Return a dictionary of information about a person"""
    person = {'firstname': firstname, 'lastname': lastname}
    return person

programmer = build_person('shem', 'mongare')
print(programmer)

print()

def build_person(firstname, lastname, age=''):
    """Return a dictionary of information about a person"""
    person = {'firstname': firstname, 'lastname': lastname}
    if age:
        person['age'] = age
    return person

programmer = build_person('shem', 'mongare')
print(programmer)

programmer = build_person('shem', 'mongare', 22)
print(programmer)

print()

# We are using the get_formated_name() function from above
while True:
    print("\nPlease tell me your name")
    print("Enter 'q' to quit at any time.")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)