players = ['Bruno', 'Cunha', 'Lammens', 'Maguire', 'Mbeumo', 'Mainoo', 'Sesko']

print(players[0:3]) # The last value is not printed
print(players[1:4])
print(players[:6])
print(players[:7])
print(players[:-1])
print(players[-3:])
print(players[:])
print(players[::2]) #[start:stop:step] we use colons and in range, commas

print('\nHere are the first three Mancunian players: ')
for player in players[:3]:
    print(player)

my_foods= ['pizza', 'chicken', 'fries', 'African nightshade']
friends_foods = my_foods[:] #copies the list my_foods, 2 separate lists are here

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's foods are:")
print(friends_foods)

# my_foods=friends_foods #Not Recommended, it sets lists to be equal

my_foods.append('carrot cake')
friends_foods.append('ice cream')

print('\nMy favorite foods are:')
print(my_foods)

print("\nMy friend's foods are:")
print(friends_foods)