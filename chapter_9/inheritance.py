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
        print(f"{miles}") #such attributes do not require the self prefix

    def fill_gas_tank(self): #used to illustrate overriding
        """Adds gas to the car"""
        print(f"The {self.make}'s gas tank has been filled!")


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
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', '2026')
print(my_tesla.get_descriptive_name())

# my_tesla.describe_battery() # accessing attribute specific to the child

my_tesla.fill_gas_tank() #method overriding

my_tesla.battery.describe_battery() #instance as an attribute
my_tesla.battery.get_range()

my_car = Car('range rover', 'sport', 2026)


my_car.increment_odometer(33)
