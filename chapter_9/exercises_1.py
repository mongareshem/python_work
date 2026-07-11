class Restaurant:
    """A model of a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialization of the attributes of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Give the general attributes of the restaurant"""
        print(f"The name of our restaurant is {self.restaurant_name.title()}.")
        print(f"The available cuisine is {self.cuisine_type.title()}.")
        print("-------------------------------------------------------------------")

    def open_restaurant(self):
        """A simple statement indicating the restaurant is open"""
        status = f"The {self.restaurant_name.title()} is open! \n\tWelcome!"
        return status


# first instance
the_restaurant = Restaurant('karen hub', 'guacamole')

#attributes
print(f"Restaurant Name: {the_restaurant.restaurant_name.title()}")
print(f"Cuisine Type: {the_restaurant.cuisine_type.title()}\n")


the_restaurant.describe_restaurant()  #call function only
print(the_restaurant.open_restaurant()) #prints return value, calls function
print("------------------------------------------------------------------")

# other instances
restaurant_2 = Restaurant("Ditaya", "chapo beans")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("Wa Jeff", "ugali matumbo")
restaurant_3.describe_restaurant()

restaurant_4 = Restaurant("aticas", "pilau beef")
restaurant_4.describe_restaurant()


class User:
    """A model of a general user"""

    def __init__(self, first_name, last_name):
        """Initializing attributes"""
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")


user1 = User("shem", "mong'are")
user1.describe_user()
user1.greet_user()

print("-------------------------------------------------------")

user2 = User("victoria", "lucy")
user2.describe_user()
user2.greet_user()