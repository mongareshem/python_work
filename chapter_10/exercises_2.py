while True:
    try:
        number_1 = int(input('Enter the first number: '))
        if number_1 == 00 :
            break
        number_2 = int(input('Enter the second number: '))
        if number_2 == 00:
            break
    except ValueError:
        print("You can only add numbers, not letters.")
    else:
        print(number_1 + number_2)

print("--------------------------------------------------------")

try:
    with open('cats.txt') as f_obj:
        cat_names = f_obj.read()

    with open('dogs.txt') as f_obj:
        dog_names = f_obj.read()
except FileNotFoundError:
    # print("The file(s) is missing!")
    pass  # The keyword used for programs that FAIL SILENTLY
else :
    print(f"\nCats: ")
    print(cat_names)

    print(f"\nDogs: ")
    print(dog_names)

# The .count('value') method
line = 'Row row row rowing your boat'
print(line.count('row'))
print(line.lower().count('row')) # lowercase catches all appearances

with open('immoralist.txt', encoding='utf') as f_obj:
    content = f_obj.read()
    print(f'\nWord count of "the": {content.lower().count('the')}')

    contents_split = content.split()
    print(f'\nWord count of entire "the":'
          f' {contents_split.count('the')}')


# The .split() method
sentence = 'Row row row, rowing your boat'
words = sentence.lower().split()
print(f"\n{words.count('row')}") #.count() doesn't take care of punctuations
