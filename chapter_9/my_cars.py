# Importing an ENTIRE MODULE
# import car
#
# my_bettle = car.Car('volkswagen', 'beetle', '2026')
# print(my_bettle.get_descriptive_name())
#
# my_tesla = car.ElectricCar('tesla', 's', 2026)
# print(my_tesla.get_descriptive_name())


# Importing SPECIFIC CLASSES (Highly Preferred!!!)
from car import Car, ElectricCar

my_bettle = Car('volkswagen', 'beetle', '2026')
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 's', 2026)
print(my_tesla.get_descriptive_name())