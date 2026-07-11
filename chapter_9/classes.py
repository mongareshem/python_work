class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")


my_dog = Dog("willie", 5) # This is an OBJECT; an INSTANCE of a class
# Python automatically RETURNS an instance (as above).

print(f"My dog is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

# Second instance
your_dog = Dog('bosco', 3)

print(f"\nYour dog's name is {your_dog.name.title()}")
print(f"Your dog's age is {your_dog.age}")
your_dog.sit()
your_dog.roll_over()
print("----------------------------------------------------------")


class Car:
    def __init__(self, make, model, year):
        """Initialize values to describe a cor"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10 # default value

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.\n")

    def update_odometer(self, mileage): # (2) The setting method
        """Set the odometer reading to a given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles): # (3) The increment method
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

# first instance
my_new_car = Car('range rover', 'sport', 2026)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer() #default odometer reading

my_new_car.update_odometer(33) #(2) Using methods to pass values for modifying attributes
my_new_car.increment_odometer(100) #(3) Using an increment method
my_new_car.read_odometer()


# Second instance
my_other_car = Car('audi', 'a4', 2025)
print(my_other_car.get_descriptive_name())

my_other_car.odometer_reading = 1000 # (1) Modifying an attribute value directly through an instance
my_other_car.read_odometer()