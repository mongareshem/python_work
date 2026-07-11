def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        # pass # no output, it does nothing and could be a reminder
    else:
        words = contents.split()
        print(f"The file {filename} has about {len(words)} words.")

# count_words('alice.txt')

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file in filenames:
    count_words(file)


# Failing silently; the pass statement
try:
    with open('shem.txt') as file_object:
        data = file_object.read()
except FileNotFoundError:
    pass
else:
    print(data)