# The class ElectricCar inherits from car, therefore,
# we have to import class Car

from car import Car

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