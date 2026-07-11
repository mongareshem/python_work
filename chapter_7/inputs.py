message  = input("Tell me something and I will repeat it back to you.")
print(message)

print(input("Tell me something and I will repeat it back to you. "))

name = input("Please enter your name: ")
print(f"Hello {name}!")

prompt = ('If you tell us who you are, we can personalize the messages you see.'
          '\nWhat is your first name? ')
name = input(prompt)
print(f"Hello {name}!")

age = input("\nWhat  is your age? ")
# print(type(age)) # everything the user enters is a string
print(age)
# print(age >= 18) # TypeError can't compare strings and integers
print(int(age) >= 18)

height = int(input("\nHow tall are you, in inches? "))

if height >= 36:
    print("You are old enough to ride!")
else:
    print("You'll be able to ride when you are a little older.")

print()

number = int(input("Enter a number and I'll tell you whether it is even or odd: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")