from name_function import get_formatted_name

print('Enter "q" at any time to quit.')
while True:
    firstname = input('\nPlease give me a first name: ')
    if firstname == 'q':
        break

    lastname = input('Please give me a last name: ')
    if lastname == 'q':
        break

    formatted_name = get_formatted_name(firstname, lastname)
    print(f'\tNeatly formatted name: {formatted_name}')