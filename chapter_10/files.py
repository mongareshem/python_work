# Reading from an ENTIRE FILE
with open('pi_digits.txt') as file_object:
     contents = file_object.read()
     print(contents)  # print(contents.rstrip())

filename = 'pi_digits.txt'  # Store filepaths in variables, always.

# Reading line by line
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())  # print(line)  # new line character at the end

# Making a list of lines
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Working with a file's contents
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()  # Removes white spaces from both r/l sides

print(pi_string)  # String; the default
# print(int(pi_string))  # Integer; works if file has PURELY DIGITS
print(len(pi_string))

# Working with a million digits
filename_2 = 'pi_million_digits.txt'

with open(filename_2) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))


# Is your birthday contained in Pi?
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


# WRITING TO A FILE
filename = "programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("\nI love creating new games.")

with open(filename, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets")
    file_object.write("\nI love creating apps that can run in a browser.")