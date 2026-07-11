from car import Car
from all_electric import ElectricCar, Battery

my_bettle = Car('volkswagen', 'beetle', '2026')
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 's', 2026)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("----------------------------------------------------------")
my_battery = Battery()
my_battery.describe_battery()

my_battery.battery_size = 85 #update battery size
my_battery.describe_battery()