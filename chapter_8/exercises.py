def display_message():
    """Print one sentence about what I am learning"""
    print("Hello everyone! I am learning about functions.")

display_message()


def favorite_book(title):
    """Prints the title of my favorite book."""
    print(f"One of my favorite books is: {title.title()}.")

favorite_book("the subtle art of seduction")
print("--------------------------------------------------------------")


def make_shirt(size, text):
    """Summary of the shirt that we are making"""
    print(f"I am making a {size} shirt printed: {text}.")

# Same outputs
make_shirt("large", "It's the economy, stupid!") #positional args
make_shirt(size="large", text="It's the economy, stupid!") #Keyword args
make_shirt(text="It's the economy, stupid!", size="large") #Keyword args
print("--------------------------------------------------------------")


def make_shirt(size="large", text="I love Python"):
    """Summary of the shirt that we are making"""
    print(f"I am making a {size} shirt printed: {text}.")

make_shirt()
make_shirt("medium")
make_shirt("small" ,"Your breakthrough is around the corner")
make_shirt(text="Awesome God!")
print("--------------------------------------------------------------")


def describe_city(city, country="kenya"):
    """A sentence giving the country in which a city is located"""
    print(f"{city.title()} is in {country.title()}.")

describe_city("nairobi")
describe_city("male", "maldives")
describe_city(city="beijing", country="china")
print("--------------------------------------------------------------")


def city_country(city, country):
    """Formatting a city and its country"""
    formatted_location = f"{city.title()}, {country.title()}"
    return formatted_location

f_location = city_country('nairobi', 'kenya')
print(f_location)
print(city_country('mombasa', country='kenya'))
print(city_country(city="arusha", country="tanzania"))
print("--------------------------------------------------------------")


def make_album(artist_name, album_title, tracks=0):
    """A dictionary describing a music album"""
    album = {
        'artist name': artist_name.title(),
        'album title': album_title.title(),
    }
    if tracks:
        album['tracks'] = tracks

    return album

album_summary = make_album('Dave', "Twenty-to-one", 22)
print(album_summary)
print(make_album("bensol", "doorstep"))
print(make_album(artist_name="Breeder lw", album_title="Gotha, gotha tena"))
print(make_album("Iyanii", 'Unanifaa', 1))
print("--------------------------------------------------------------")


while True:
    artist = input("\nEnter artist's name: ")
    if artist == 'quit':
        break

    album_name = input("Enter the albums's name: ")
    if album_name == 'quit':
        break

    print(make_album(artist, album_name))

    summary = make_album(artist, album_name)
    for k,v in summary.items():
        print(f"{k}: {v}")
print("--------------------------------------------------------------")


def show_magicians(magicians_names):
    """Printing out a list of magicians"""
    for magician_name in magicians_names:
        print(magician_name.title())

magicians = ['oz pearlman', 'david', 'kajairo', 'peter']
show_magicians(magicians)
print()
show_magicians(['oz pearlman', 'kajairo', ])
print("--------------------------------------------------------------")

great_magicians = []
def make_great(great_magician_names):
    """Moving magicians to the Greatness level"""
    for great_magician_name in great_magician_names:
        print(f"The Great {great_magician_name.title()}")
    while great_magician_names:
        current_magician = great_magician_names.pop()
        great_magicians.append(current_magician)

# make_great(magicians) # Passed an ORIGINAL list of magicians

# print(f'Magicians: {magicians}') #original list, now empty
# print(f"Great Magicians: {great_magicians}") #new list
#
# show_magicians([]) # No iterable -> No output; Same as below
# show_magicians(magicians) #Empty due to the transfer
print("--------------------------------------------------------------")


make_great(magicians[:]) # A COPY[:] of magicians
print(f"New List: {great_magicians}") # Started empty, now modified
print(f"Original list: {magicians}") # Unchanged