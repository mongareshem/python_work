countries = ['Kenya', 'USA', 'China', 'Maldives', 'Nigeria','Egypt','South Africa','Qatar', 'Zambia', ]
print(countries)

countries.append('Rwanda')
print(countries)

countries.insert(2, 'Colombia')
print(countries)

del countries[5]
print(countries)

countries.pop()
print(countries)

countries.pop(5)
print(countries)

countries.remove('South Africa')
print(countries)

print(sorted(countries))
print(sorted(countries, reverse=True))

countries.reverse()
print(countries)

countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)

print(len(countries))