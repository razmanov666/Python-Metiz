import sys
sys.path.insert(0, '/home/kurama/Документы/Training/Python/6-10/9/classes')
from cls_electric_car import *

tesla = ElectricCar('tesla', 's', 2016)
tesla.battery.get_range()
tesla.battery.update_batter()
tesla.battery.get_range()