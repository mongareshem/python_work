"""A set of classes used to represent gas and electric cars."""

class Car:
    def __init__(self, make, model, year):
        """Initialize values to describe a cor"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10  # default value

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.\n")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            distance = 240
            print(f"This car can go approximately {distance} miles on a full charge.")

        elif self.battery_size == 85:
            distance = 270
            print(f"This car can go approximately {distance} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class
            Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        # self.battery_size = 70 # attribute specific to the child class
        self.battery = Battery() # instance as an attribute

    def fill_gas_tank(self): # method overriding
        """Electric cars do not have gas tanks"""
        print(f"This {self.make} doesn't need a gas tank!")