def greet_user(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        print(f"Hello, {name.title()}!")

usernames = ['hannah', 'ty', 'marie']
greet_user(usernames)

print("--------------------------------------")

unprinted_designs = ['iPhone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

print("---------------------------------------")

def print_models(unprinted_designs, completed_models):
    """
        Simulate printing each design, until none are left
        Move each design to completed_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were completed"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iPhone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
#print_models(unprinted_designs[:], completed_models) #This line passes a copy
show_completed_models(completed_models)

print("-------------------------------------------------")
print(unprinted_designs) # The list is unchanged if a copy is passed

print()

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza("green peppers")
make_pizza("extra cheese", "anchovies", "pepperoni")

print("-------------------------------------------------")

def make_pizza(*toppings):
    """Summarize the pizza we are about to make: """
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")

make_pizza("green peppers")
make_pizza("extra cheese", "anchovies", "pepperoni", "mushrooms")

print("-------------------------------------------------")

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make: """
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(12,"green peppers")
make_pizza(16, "extra cheese", "anchovies", "pepperoni", "mushrooms")

print("---------------------------------------------------")

def build_profile(firstname, lastname, **user_info):
    """Building a dictionary that contains everything we know about a user."""
    profile = {}
    profile['firstname'] = firstname
    profile['lastname'] = lastname
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("shem", "mong'are",
                             location='nairobi', field="engineering")
print(user_profile)

u_profile = build_profile("shem", "mong'are")
print(u_profile)