class Restaurant():
    """Класс для ресторанов"""
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Инициализация ресторана"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Краткое описание ресторана"""
        print ('Restaurant has name ' + self.name.title() +  
                ' and cocking ' + self.type + ' food.')

    def open_restaurant(self):
        """Ресторан открыт"""
        print ('Restaurant ' + self.name.title() + ' is opened!')
    
    def read_number_served(self):
        """Выводит кол-во обслуженных клиентов"""
        print ('This restaurant has ' + str(self.number_served) + ' ckients on it.')

    def set_number_served(self, cliens):
        """
        Устанавливает заданное значение обслуженных клиентов.
        """
        self.number_served = cliens
    
    def incriment_number_served(self, cliens):
        """
        Увеличивает значение обслуженных клиентов с заданным приращением 
        """
        self.number_served += cliens