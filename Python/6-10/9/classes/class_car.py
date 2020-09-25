class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_desciptive_name(self):
        """Вызывает аккуратно отформатированное описание"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях"""
        print ('This car has ' + str(self.odometer) + ' miles on it.')

    def update_odometer(self, miles):
        """
        Устанавливает заданное значение на одометре.
        При попытке открутки, изменения отклоняются.
        """
        if miles >= self.odometer:
            self.odometer = miles
        else:
            print("You can't roll back an odometer!")
    
    def incriment_odometer(self, miles):
        """
        Увеличивает показания одометра с заданным приращением 
        """
        self.odometer += miles