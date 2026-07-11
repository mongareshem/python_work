# Sorting lists permanently using the .sort() method
cars=['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#Sorting a list temporarily using the sorted() function
cars=['gle', 'range rover', 'mazda', 'volvo']

print(f'\nHere is the original list:')
print(cars)

print(f'\nHere is the sorted list:')
print(sorted(cars))

print(f'\nHere is the original list again')
print(cars)

#Printing a list in reverse order using the reverse() method
cars.reverse()
print(cars)

#Finding the length of a list using the len() function
number_of_cars=len(cars)
print(number_of_cars)

