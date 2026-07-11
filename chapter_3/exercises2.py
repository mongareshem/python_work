places = ['Maldives', 'Miami, Florida', 'Beijing', 'Diani', 'Manchester']
print(places)
print()

print(sorted(places))
print(places)
print()

print(sorted(places, reverse=True))
print(places)
print()

places.reverse() #Sorts a list backwards, NOT alphabetically.
print(places)
places.reverse()
print(places)
print()

places.sort()
print(places)
places.sort(reverse=True)
print(places)