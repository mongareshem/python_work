current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# prompt = "Tell me something and I'll repeat it back to you"
# prompt += "\nEnter 'quit' to end the program: "
#
# message = ""
# while message != 'quit':
#     message = input(prompt)
#
#     if message != 'quit':
#         print(message)

print()

prompt = "Tell me something and I'll repeat it back to you"
prompt += "\nEnter 'quit' to end the program: "

active = True #This is a flag
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

print()

prompt = ('\nPlease enter the name of a city you have visited'
          '\n Enter quit when you are finished.')
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")

print()

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)
