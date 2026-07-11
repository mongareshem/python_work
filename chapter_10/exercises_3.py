import json

filename = 'favorite_number.json'

favorite_number = input("Favorite Number: ")
with open(filename, 'w') as fileobject:
    json.dump(favorite_number, fileobject)

with open(filename, 'r') as fileobject:
    favorite_number = json.load(fileobject)
    print(f"I know your favorite number, it is {favorite_number}.")

print("------------------------------------------------------------")

filename= 'fav_number.json'
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)

except FileNotFoundError:
    number = input("What is your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    print(f"We'll remember {number} is your favorite!")
else:
    print(f"Your favorite number is: {number}.")