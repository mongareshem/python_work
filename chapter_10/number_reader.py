import json

filename = 'numbers.json'

with open(filename) as file_object:
    numbers = json.load(file_object)
print(numbers)  # print statement outside; print after reading (indentation/closed)

# Always do file operations inside and data operation outside