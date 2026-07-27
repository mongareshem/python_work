print('Give me two numbers and I will divide them')
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break

    print(int(first_number)/int(second_number))