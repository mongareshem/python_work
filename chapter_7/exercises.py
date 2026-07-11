car = input("What kind of car would you like to rent? ")
print(f"Let me see if I can find you a {car.title()}.")

number_of_people = input("\nHow many people are in your dinner group? ")
if int(number_of_people) > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready!")

number = int(input("\nEnter a number: "))
if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")

print()

active = True
while active:
    topping = input("\nEnter your preferred pizza topping: ")
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

print()

ticket_on_sale = True
while ticket_on_sale:
    age = input("Enter your age: ")
    if age == 'quit':
        break
    else:
        if int(age) < 3:
            print("Your ticket is $0.")
        elif 3 <= int(age) <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

print()

topping = ""
while topping != 'quit':
    topping = input("\nEnter your preferred pizza topping: ")
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")

print ()

i = 0
while i <= 5:
    print(i)
    i += 1 # If this line is missed, we have an INFINITE LOOP