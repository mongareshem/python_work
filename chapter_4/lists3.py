magicians = ['alice', 'oz', 'david', 'carolina']

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick {magician.title()}.\n")

print('Thank you everyone, that was a great magic show!')

for value in range(1, 6): #The output never contains the end value.
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2)) # range(start, stop, step)
print(even_numbers)

odd_numbers = list(range(1,11,2))
print(odd_numbers)

squares = []
for number in range(1, 11):
    squares.append(number**2)
print(squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

fourth_powers = [value**4 for value in range(1, 11)]
print(fourth_powers)