# print(5/0)  #ZeroDivisionError

# Handling the ZeroDivisionError; TRY-EXCEPT block
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print("-----------------------------------------------------")

# Handling the ZeroDivisionError; TRY-EXCEPT-ELSE block
print("\nGive me 2 numbers and I will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break

    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
print("-------------------------------------------------------")


# Handling the FileNotFoundError
filename = 'alice.txt'

try:
    with open(filename, encoding="utf-8") as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
else:
    words = contents.split()
    print(f"The text has {len(words)} words.")


# The method .split()
title = 'Alice in Wonderland!'
title_split = title.split()
print(title_split)  # print(title.split())

# Analyzing entire texts using the .split() method
