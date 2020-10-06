from class_car import *



class ElectricCar(Car):
    """Представляет аспекты машины специфические для электромобиля"""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery() 

class Battery():
    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора"""
        self.battery_size = battery_size

    def get_range(self):
        """Выводит приблизительный запас хода аккумулятора."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
             range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print (message)
    
    def update_batter(self):
        """Присваивает запасу хода аккумулятора значение 85"""
        self.battery_size = 85

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
