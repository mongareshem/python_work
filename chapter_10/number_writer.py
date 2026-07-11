import json

filename = 'numbers.json'

numbers = [2, 3, 5, 7, 11, 13]

with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)