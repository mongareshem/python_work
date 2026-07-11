class Restaurant:
    """A model of a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialization of the attributes of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Give the general attributes of the restaurant"""
        print(f"The name of our restaurant is {self.restaurant_name.title()}.")
        print(f"The available cuisine is {self.cuisine_type.title()}.")
        print("-------------------------------------------------------------------")

    def open_restaurant(self):
        """A simple statement indicating the restaurant is open"""
        status = f"The {self.restaurant_name.title()} is open! \n\tWelcome!"
        return status

    def customers_served(self):
        """Prints the number of customers served"""
        print(f"The restaurant has served {self.number_served} customers today.")

    def set_number_served(self):
        """Sets the number of customers that have been served"""
        self.number_served = 30

    def increment_number_served(self, customers):
        """Increases the number of the people served"""
        self.number_served += customers


restaurant = Restaurant("aticas", "pilau beef")

restaurant.customers_served()

restaurant.number_served = 10
restaurant.customers_served()

restaurant.set_number_served()
restaurant.customers_served()

restaurant.increment_number_served(50)
restaurant.customers_served()


class User:
    """A model of a general user"""

    def __init__(self, first_name, last_name, login_attempts):
        """Initializing attributes"""
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.login_attempts = login_attempts

    def describe_user(self):
        """A brief description of the user using the first and last names"""
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        """A greeting to the user"""
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        """A method to increase the login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """A method that resets the login attempts to 0"""
        self.login_attempts = 0


user = User("shem", "mongare", 0)

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"\nUser Login Attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"\nUser Login Attempts: {user.login_attempts}")


class IceCreamStand(Restaurant):
    """A model of a special kind of restaurant - ice cream"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize inherited attributes and specify own"""
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = ['strawberry', 'vanilla', 'chocolate', 'banana']

    def display_flavors(self):
        """Show the different kind of flavors that we have."""
        print(f"\nWe have the following flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor}")


ice_cream = IceCreamStand('scoops and spoons',
                          'ice cream')

ice_cream.display_flavors()


class Privileges:
    """A separate class for all the special privileges the admin has"""

    def __init__(self, privileges):
        """Initialize the attribute privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Print out the privileges of the admin"""

        print(f"\nThe following are the Admin privileges: ")
        for privilege in self.privileges:
            print(f"\t\t{privilege.capitalize()}.")

class Admin(User):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)

        special_permissions = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges(special_permissions)


admin = Admin('shem', "mong'are", 1)
admin.privileges.show_privileges()

# privileges = Privileges(['add user', 'ban user', "post"])
# privileges.show_privileges()