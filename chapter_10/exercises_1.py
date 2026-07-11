# READING FROM A FILE

filename = 'learning_python'

# Reading the entire file
with open(filename) as fileobject:
    contents = fileobject.read()

print(contents)
print("---------------------------------------------\n")

# Looping through the file
with open(filename) as fileobject:
    for line in fileobject:
        print(line.rstrip())
print("--------------------------------------------\n")


# Storing contents in a list
with open(filename) as fileobject:
    lines = fileobject.readlines()

python_string = ''
for line in lines:
    python_string += line.strip()

print(python_string)
print("----------------------------------------------\n")


# Using the .replace(a, b) method; a replaces b
message = "I really like dogs.\n"
message.replace('dogs', 'cats')
print(message)

with open(filename) as fileobject:
    for line in fileobject:
        print(line.replace('Python', 'C').strip())


# WRITING TO A FILE
filename = 'guest.txt'
name = input("\nWhat is your name? ")

with open(filename, 'w') as fileobject:
    fileobject.write(name)

#Guest Book
filename = 'guest_book.txt'
while True:
    user_name = input("What is your name? ")

    if user_name == 'q':
        break
    else:
        print(f"Hello {user_name}!")

    with open(filename, 'a') as f_obj:
        f_obj.write(f"{user_name}\n")

# Programming reasons
filename = 'reasons.txt'
while True:
    reason = input("Why do you like programming? ")

    if reason == 'q':
        break
    else:
        print(f"{reason}")

    with open(filename, 'a') as f_obj:
        f_obj.write(f"{reason}\n")
