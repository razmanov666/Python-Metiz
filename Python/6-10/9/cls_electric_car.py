from class_car import *

class ElectricCar(Car):
    """Представляет аспекты машины специфические для электромобиля"""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")