bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

print()

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])
print(bicycles[-3])

message = "My first bicycle was a " + bicycles[0].title()
print(message)
print(f'My ideal bicycle is a {bicycles[-1]} one.')

print()

# Changing, Adding and Removing items from a list

# CHANGING
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)

motorcycles[0] = 'Boxer'
print(motorcycles)

print()

# ADDING
# using .append()
motorcycles.append("Ducati")
print(motorcycles)

bikes=[]
bikes.append("Honda")
bikes.append("Yamaha")
bikes.append("Suzuki")
print(bikes)

# using .insert(index, value)
motorcycles.insert(3, 'Bat Mobile')
print(motorcycles)

bikes.insert(0, "Ducati")
print(bikes)

print()

# REMOVING
# 1. By position
# Using del
del bikes[0]
print(bikes)

del bikes[2]
print(bikes)

del motorcycles[-2]
print(motorcycles)

# Using pop()
# To remove the last
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print(f'The last motorcycle I owned was a {motorcycles.pop().title()}.')

#To remove at any index
first_motorcycle = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_motorcycle}.')
print(motorcycles)

# 2. By value
# Using remove()
motorcycles = ['Honda', 'Yamaha', 'Suzuki', 'Ducati']
too_expensive = "Ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\n A {too_expensive} is too expensive for me.')