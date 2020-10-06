from cls_electric_car import *

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_desciptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.battery_size = 85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()